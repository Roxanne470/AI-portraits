# AI-portraits

## Generating your own portraits

Let's get you some hands-on experience with generative AI! 

### Step 1: Clone the repository

Open a terminal on your computer and clone this repository by 

`git clone https://github.com/Roxanne470/AI-portraits.git`

The AI-portraits folder that's downloaded to your current directory contains a folder called app which has the scripts for generating our AI portraits and a requirements.txt file which will be used to create a Python virtual environment for our project.

Feel free to open the scripts in the `app` folder to get a grip on what's happening inside our generative AI application.

### Step 2: Create the virtual environment

It's a good habit to create a new virtual environment for a new project. This makes sure that you have the required software dependencies of the projects isolated in their own environments and not interfering with each other. 

First, check if you have the tool virtualenv installed on your computer by running virtualenv in your terminal. If the displayed message is the usage of virtualenv, then you are good. If it says command not found: virtualenv, then you need to run this first:

`pip3 install virtualenv`

(Once it's finished, check again by running the command virtualenv to make sure you have the tool to create isolated Python environments.)
Next, in the terminal (make sure you are still in the AI-portraits folder), run these two commands to create a virtual environment env and activate it.

`virtualenv env` and  

`source env/bin/activate`

Once you see (env)at the beginning of a new line in your terminal, you've successfully activated it.

Now, we can install all the required Python packages for our generative AI into env by (give it some time to install, go grab a coffee if you can):

`pip3 install -r requirements.txt`

Once the installation process is completed, we will have the environment for running the generative AI!

### Step 3: Execute the generative AI scripts

Now, go to the `app` folder (`cd app`) and run the demo.pyfile.

`python3 demo.py`

It will download the model weights file `u2net.tgz` and load the weights into a U-squared network architecture initialized from `model.py`.
The script will take any new jpeg images from the `test_photosfolder` and generate a portrait (using the U-squared network) for each test image. The generated portraits will be saved into the `test_resultsfolder`.
