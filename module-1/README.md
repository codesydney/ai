# Module 1 - Fundamentals

Although this is a Generative AI course, we will need some basic skills to get started.

## Software Development Fundamentals
- This course will mainly use **Python** for all the tasks that require coding. 
- As with any software development project, **version control** is essential. We will be using **Git** for this purpose.
- This study group is a collaborative effort and we hope that you will collaborate and work together on the included projects. To make it easier, please use the group's **Discord channel** , **Github** to share your work, and **LinkedIn** to share you learnings.
- The final project will be an **end-to-end Generative AI solution** and will require some web work. There are tech stack options available to you depending on your dev background.
- And finally in any software development work, **having soft skills** are equally as important as the technical skill. Things like communication, teamwork and time management are crucial soft skills in software development.   

## Jupyter Notebooks

We recommend that everyone taking this course uses **[Visual Studio Code](https://code.visualstudio.com/)** with the following list of useful extensions:

- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)


## Preparing your Python environment

We recommend that you use [Pyenv](https://github.com/pyenv/pyenv) (Optional) to manage your Python versions. This will allow you to easily switch between different versions of Python and also manage your virtual environments.

And before starting any Python development, it is **best practice** to create a **virtual environment**. This will allow you to isolate your project dependencies from your system dependencies.

If you are beginner to Python, better to get used to working with virtual environments from the start so that this will become second nature to you. 

Typically this can be done like so:

```bash
pyenv versions
pyenv install 3.12.2
pyenv local 3.12.2 # setup your local Python version
python -m venv .venv # create a virtual environment
source .venv/bin/activate # activate the virtual environment and start using the environment
```

## Assignment
- Install **Visual Studio Code** with the extensions listed above
- Install **Pyenv**, **create and activate a virtual environment** for Python 3.12
- **Fork** this course in your personal Github 
- **Star** this course in Github
- Join the **[Discord channel](https://discord.com/channels/1041795715757789204/1094455854897573908)** and introduce yourself
- Let others know what you are learning now and **LinkedIn** is great for this
- Connect with your study group members on **LinkedIn**, and [with me too](https://linkedin.com/in/joreyes)!

## FAQ
### **Q:** Is it okay if i don't use **pyenv**?
- **Pyenv** is used to manage different versions of Python for your project. But for the purposes of building generative AI apps, changing the Python version is not that important. Just make sure that you are on a recent version, say >= Python 3.10. We have marked **Pyenv** as optional because it is not a requirement for this course. But it is a good practice to use it.

### **Q:** How about **virtual environment**, is it required?
- Yes, it is a best practice to use virtual environments. This will allow you to isolate your project dependencies from your system dependencies. This will also help you to avoid conflicts between different projects that you are working on.

- It is best practice to use virtual environments from the start so that this will become second nature to you.

### **Q:** Will this be an individual project or collaborative? Are we going to present/demo the project?
- It is entirely up to you, if you want to work by yourself or collaborate with someone in this cohort. In my opinion maybe the last project can be worth a collaboration, entirely up to you. As for presentation of the demo project, we might not have the time to do that?

- As we only have 30 mins catch up each week, we don't have much time + I also have a short (~15 min) presentation for each module. However, no stopping anyone from making a presentation-worthy notebook so you can add in your personal github as part of your portfolio? Let me know what others feel about presenting/demoing the projects?

### **Q:** Is it OK to NOT use local LLMs? My machine is not powerful enough for them. 
- Yes, it is okay to use online LLMs. The code to access the models is mostly the same, thanks to the OpenAI compatibility API and other libraries. However, this will mean that you will need to pay for these services, on a positive note, your notebooks will run much faster that with the local LLMs.
