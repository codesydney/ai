# Module 2 - Generative AI Basics

This **Generative AI learning path** is designed to help you build your knowledge and skills in Generative AI, but instead of connecting to a cloud-based model, we will be using a **Local Large Language Model (Local LLM)** for our learning journey. This has a few advantages, such as privacy, cost, and the ability to use a wide variety of local LLMs. In other words, running your local LLM enables the **democratisation of AI**, allowing you to experiment and use different models without the worry of incurring high costs.

**Privacy**: You can use your own data and models without sharing them with a cloud provider.

**Cost**: You can run your models on your own hardware, which can be more cost-effective than cloud-based solutions, so you can experiment with different models without the worry of incurring high costs.

**Variety of LLMs**: There are many LLMs available that can be run locally, and you can choose the one that best fits your needs. You can also customise and fine-tune these models to suit your specific requirements.

## Introduction to Generative AI

Generative AI refers to a type of artificial intelligence that can create new data, such as images, videos, music, or text, rather than simply processing and analysing existing data. This is achieved through various algorithms and techniques, including machine learning, deep learning, and neural networks.

Generative AI burst into the mainstream towards the end of 2022, with the release of OpenAI's GPT-3, which is one of the most advanced generative models available. Since then, there have been many other models released, each with its own unique capabilities and use cases.

### Open AI Chat Completions API

OpenAI built the [chat completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) shortly after the release of GPT-3, which allows developers to build chatbots and other conversational AI applications using the GPT-3 model. This API has been used to build a wide range of applications, from customer service chatbots to creative writing tools.

Many other LLM models have been released since then, each with its own unique capabilities and use cases. However, these models have their own APIs, which can be challenging to use and integrate into your applications.

### New Generation AI Developer Tools

This is where this new generation developer tools come in. Applications like [LM Studio](https://lmstudio.ai/) and [Ollama](https://ollama.com/) enable developers to run these models locally, making it easier to experiment with different models and integrate them into your applications. In addition to that, they have Open AI compatibility, so that irregardless of the model you are using, you can still use the Open AI API.

This is a game changer, because, it will **allow one to experiment with different models without the need to change the code**. 

For this learning path, we will be using **[LM Studio](https://lmstudio.ai/)** to build our Generative AI applications.

## Access to LLM using Python

We will be using Python to access our Local LLM through LM Studio's OpenAI compatibility API. The OpenAI compatibility API allows you to use the same code to access different models, giving the developer the flexibility to experiment with different models without changing the code.

## Online vs Local LLM (LM Studio)

There are two main ways to access LLMs from our application: online and locally. Online LLMs are hosted on the cloud (ChatGPT, Anthropic, Google's Gemini, Meta's Llama, AWS Bedrock, etc) and can be accessed via an API, while local LLMs are run on your own hardware and can be accessed via a local API. Cloud LLMs can be challenging as they will have a variety of API standards, but there are integrations that make them OpenAI compatible.

So regardless of Online LLM or Local LLM, the code to access the models is the same, thanks to the OpenAI compatibility API and other libraries . This means that whatever you build locally, with little change, you can easily deploy it to the cloud. 

Cloud deployment of your Generative AI is beyond the scope of this learning path, but it is something you can explore once you have built your Generative AI applications, or perhaps another learning path.

## Setting up your local LLM

For this learning path, we will be using a tool called **[LM Studio](https://lmstudio.ai/)** to access our Local LLM. LM Studio is a powerful tool that allows you to run your LLM locally and access it through a simple API. It also has OpenAI compatibility, so you can use the same code to access different models.

Initially we will start with the simple use case of accessing an LLM like in a chatbot scenario. We will then build on this to more complex use cases like Retrieval-Augmented Generation (RAG) and Vector Databases.

While LM Studio is primarily a desktop application that will work with **Windows**, **Mac** (M* Apple silicon) and **Linux**, it recently released a CLI version - **[LM Studio CLI](https://lmstudio.ai/blog/lms)**, so that you can run and control it programmatically. 

**We will be covering in more detail how to set up your local LLM dev environment as part of this module.**

### Note: 

## Generative AI Libraries

We will also be covering some of the popular Generative AI libraries that you can use to build your Generative AI applications. These libraries provide a wide range of tools and features that can help you build and deploy your Generative AI applications quickly and easily.

Tools like **[LangChain](https://www.langchain.com/)** and **[LlamaIndex](https://www.llamaindex.ai/)** are popular libraries that can be used to build Generative AI applications. We will be covering these libraries and more in a bit more detail in the next few modules.

Later on, we will also be covering more advanced topics such as Vector Databases and Retrieval-Augmented Generation (RAG) options. 

## Assignment
- Install **LM Studio** and **LM Studio CLI** on your local machine. For those that are using a cloud-based LLM, you can skip this step.
- Copy the [first exercise](1-local-llm-openai-compatibility.ipynb) to `my-notebooks` folder. Work on the exercise, but instead of a Llama 3 LLM, use another one from LM Studio. If you are using a cloud-based LLM, you can see if there is another LLM model that you can connect to. 
- Copy the [second exercise](2-local-llm-chatbot.ipynb) to `my-notebooks` folder. Work on the exercise with different values in the LM Studio API.
- If you have more time, perhaps you can try to build another version of the second exercise, but instead of LlamaIndex, maybe use LangChain?
- Reflect on your learnings and report back to the group in the Discord channel.

