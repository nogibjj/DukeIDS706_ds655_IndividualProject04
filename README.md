# Individual Project #4: Auto Scaling Flask App Using a Serverless Platform

[![Install](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/01_Install.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/01_Install.yml)
[![Black Formatter](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/02_Format.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/02_Format.yml)
[![Lint](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject02/actions/workflows/03_Lint.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject02/actions/workflows/03_Lint.yml)
[![Test](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/04_Test.yml/badge.svg)](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject03/actions/workflows/04_Test.yml)

# Sentence Completion using GPT-2

#

Input Screen (Generated from `index.html`)

![image](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject04/assets/143483773/b6680179-b6f2-4d9c-b4be-0bc85a61f63e)


Text Entered: *"My Name is Divya and I "*

Output Screen (Generated from `result.html`)

![image](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject04/assets/143483773/090f5ddf-0cc9-47cf-8911-7d12538a06ca)


# Components:

### Flask App
The Flask application serves as the backend for the web application. It exposes two routes: the root ("/") route that renders the `index.html` template, and the "/analyze" route that accepts POST requests. When a POST request is sent to the "/analyze" route, the application takes the text from the request, sends it to the [*GPT-2*](https://huggingface.co/gpt2) model hosted on Hugging Face's API for sentence generation, and then renders the `result.html` template with the original text and the generated text.

![image](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject04/assets/143483773/a4a264b1-3d86-44b5-b463-bf68258c7fd4)


### Use of DockerHub
DockerHub is used to store the Docker image of the application. Docker is a platform that allows us to package the application along with all of its dependencies into a standardized unit (a _Docker image_) for software development. [DockerHub](https://hub.docker.com/) is a cloud-based registry service that allows us to link to code repositories, build images and test them, stores manually pushed images, and links to Docker Cloud so you can deploy images to hosts.

![image](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject04/assets/143483773/7ede9da5-b61c-497a-a81d-95354191cc71)


### Azure Web App
[Azure Web App](https://azure.microsoft.com/en-us/products/app-service/web) is a fully managed platform for building, deploying, and scaling web apps. It can be used to host the Dockerized Flask application. It provides automatic scaling, patching, CI/CD integration, and advanced security policies. In this case, Azure Web App is used to pull the Docker image from DockerHub and deploy it, making the sentence generation application accessible on the internet in the link [ds655-ind4.azurewebsites.net](https://ds655-ind4.azurewebsites.net/)

![image](https://github.com/nogibjj/DukeIDS706_ds655_IndividualProject04/assets/143483773/00ed169d-975e-462c-b66d-b775bbc3270c)

### Video Demo 
The demo can be found at - [Link]()
















#

## File Index

Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions


## 4. Resources
  -  This folder contains any other files relevant to this project. Currently, I have added -


## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  
  The `.devcontainer` folder mainly contains two files - 
  * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
  * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
