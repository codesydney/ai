import chainlit as cl

from llama_index.core import (
    Settings,
    StorageContext,
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from llama_index.core.query_engine.retriever_query_engine import RetrieverQueryEngine
from llama_index.llms.lmstudio import LMStudio
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.postgres import PGVectorStore
import psycopg2
from sqlalchemy import make_url

BASE_DIR = "./data"

def setup_vector_db():
    """
    Setup the Postgres database for storing vector embeddings
    """
    try:
        pg_pw = "mysecretpassword"
        pg_db = "vector_store"
        connection_string = f"postgresql://postgres:{pg_pw}@localhost:5432"
        db_name = pg_db
        conn = psycopg2.connect(connection_string)
        conn.autocommit = True

        with conn.cursor() as c:
            c.execute(f"DROP DATABASE {db_name} WITH (FORCE);")
            c.execute(f"CREATE DATABASE {db_name};")

        conn.commit()
        conn.close()
        return connection_string, db_name
        
    except Exception as e:
        print(e)

def setup_embedding_model():
    """
    Setup the Hugging Face embedding model.
    """
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    text_embedding = embed_model.get_text_embedding("Once upon a time, there was a cat.")
    print(text_embedding[:5])
    print(f"Emedding length: {len(text_embedding)}")
    vector_size = len(text_embedding)
    
    return embed_model, vector_size
    
def setup_global_settings(embed_model):
    """
    Setup global settings for the Llama Index.
    """
    Settings.llm = LMStudio(
        model_name="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M-take2.gguf",
        base_url="http://localhost:1234/v1",
        temperature=0,
        # set this parameter to increase request time out
        request_timeout=100,
    )
    Settings.embed_model = embed_model
    Settings.context_window = 8192

def simple_RAG(vector_size, connection_string, db_name):
    """
    Simple Retrieval Augmented Generation (RAG) using Llama Index.
    """

    url = make_url(connection_string)
    print(f"Url {url}")
    
    vector_store = PGVectorStore.from_params(
        database=db_name,
        host=url.host,
        password=url.password,
        port=url.port,
        user=url.username,
        table_name="simple_rag",
        embed_dim=vector_size
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    nodes = ingest_documents(BASE_DIR)
    
    print(f"Number of nodes: {len(nodes)}")
    print()
    for node in nodes:
        print(f"Node text: {node.text}")
        print(f"Node length: {len(node.text)}")
        print()

    index = VectorStoreIndex.from_documents(nodes, storage_context=storage_context, show_progress=True)
    return index

def ingest_documents(directory):
    
    """
    Ingest documents from a directory into the vector store. 
    """
    reader = SimpleDirectoryReader(input_dir=directory)
    return reader.load_data(show_progress=True)

try:
    connection_string, db_name = setup_vector_db()
    embed_model, vector_size = setup_embedding_model()
    setup_global_settings(embed_model)
    index = simple_RAG(vector_size, connection_string, db_name)
    query_engine = index.as_query_engine(
        verbose=True,
        streaming=True,
        similarity_top_k=2)
except Exception as e:
    print(e)

@cl.on_chat_start
async def start():
    """
    Start the chat session.
    """

    cl.user_session.set("query_engine", query_engine)

    await cl.Message(
        author="Assistant", content="Hello! Im an AI assistant. I have ingested Attention is All You need PDF. How may I help you?"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """
    Main function to handle the user's query.
    """
    query_engine = cl.user_session.get(
        "query_engine")  # type: RetrieverQueryEngine

    msg = cl.Message(content="", author="Assistant")

    res = await cl.make_async(query_engine.query)(message.content)

    for token in res.response_gen:
        await msg.stream_token(token)
    await msg.send()
