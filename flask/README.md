## Steps for setting up flask server

1. Install the latest version of [python 3.0+](https://www.python.org/downloads/)

2. Clone this repository



3. Navigate into the flask directory of this project. Create a virtual environment with the following commands.

**Note:** You may need to use pip3 instead of pip

Skip this installation command if you already have this package
```
$ pip install virtualenv
```

Activating the environment:

For Mac/Linux/WSL users:
```
$ virtualenv env
$ source env/bin/activate
```
For Windows users:
```
$ virtualenv env
$ env\Scripts\activate
```


4. Now that you created your virtual environment and activated it, we want to install the neccessary packages.

```
$ pip install -r requirements.txt

```

## Running the live server on your pc

The virtual environment has to be running. After it's activated enter the following:

For Mac/Linux/WSL users:
```
$ flask run
```
**Note** WSL = Windows Subsystem for Linux

For Windows users:
```
$ set FLASK_APP=main.py
$ flask run
```