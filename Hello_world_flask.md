# Hello World in Flask

## Installing Flask


### _=> Prerequisites_
1. Install the Python extension.
2. Install a version of Python 3 (for which this tutorial is written). Options include:
   -(All operating systems) A download from python.org; typically use the Download Python 3.9.1 button that appears first on the page (or whatever is the latest version).
   -(Linux) The built-in Python 3 installation works well, but to install other Python packages you must run sudo apt install python3-pip in the terminal.
   -(macOS) An installation through Homebrew on macOS using brew install python3 (the system install of Python on macOS is not supported).
   -(All operating systems) A download from Anaconda (for data science purposes).
3. On Windows, make sure the location of your Python interpreter is included in your PATH environment variable. You can check the location by running path at the command prompt. If the Python interpreter's folder isn't included, open Windows Settings, search for "environment", select Edit environment variables for your account, then edit the Path variable to include that folder.

### _=> Creating a virtual Environment_
Create a project folder and a venv folder within:
>mkdir myproject<br/>
>cd myproject<br/>
>python3 -m venv venv<br/>

On Windows:
>py -3 -m venv venv

If you needed to install virtualenv because you are on an older version of Python, use the following command instead:
>virtualenv venv<br/>

On Windows:
>\Python27\Scripts\virtualenv.exe venv

### _=> Activation of the environment_
Before you work on your project, activate the corresponding environment:
>. venv/bin/activate

On Windows:
>venv\Scripts\activate<br/>
Your shell prompt will change to show the name of the activated environment.

### _=> Installation_
Python comes with a package manager named pip. It uses the the official Python package repository named PyPI.
To install a Python package, you need to open a terminal. This varies per operating system.

-On Linux you can press the key combination Ctrl+Alt+T to open a terminal.
-On Mac OS X, press the keys CMD + Space to open spotlight search, and type terminal and hit return.
-On Windows, press the keys Super + R and type cmd and press the enterk ey.

You can install a Python package with the command:
>pip install <package-name>

In this case you want to type the command:
>pip install flask

Then verify it’s installed correctly. Type the command
>(venv) ➜  flaskexample python3

The output should be:

> \>\>\> import flask<br/>
> \>\>\>

If you see the output below, it means flask is not installed in the virtual enviroment.
>Python 3.7.3 (default, Aug 20 2019, 17:04:43)<br/>
>[GCC 8.3.0] on linux<br/>
>Type "help", "copyright", "credits" or "license" for more information.<br/>
>\>\>\> import flask<br/>
>Traceback (most recent call last):<br/>
>  File "<stdin>", line 1, in <module><br/>
>ModuleNotFoundError: No module named 'flask'<br/>
>\>\>\><br/> 

## Routes and view Functions

The Flask application keeps a mapping of URLs to Python functions. The association between a URL and the function that handles it is called a ***route***. 
The most convenient way to define a route in a Flask application is through the 
app.route decorator exposed by the application instance. 
Example:
>@app.route('/') <br/>
>def index():<br/> 
>&emsp;return 'Hello World!'<br/> 

The app.route decorator is the preferred method to register view 
functions, Flask also offers a more traditional way to set up the application routes 
with the app.add_url_rule() method, which in its most basic form takes three argu‐ 
ments: the URL, the endpoint name, and the view function. The following example 
uses app.add_url_rule() to register an index() function that is equivalent to the 
one shown previously: 
>def index():<br/>
>&emsp;return 'Hello World!' 

app.add_url_rule('/', 'index', index) 
Functions like index() that handle application URLs are called ***view functions***.



## Hello World in Flask

Now after installation we can finally make our first app using flask.
Follow below steps to make a simple Hello world app using in flask.

Use the line below to import Flask in Python.
>from flask import Flask<br/>

Create app, that hosts the application
>app = Flask(__name__)<br/>

Then you need a route that calls a Python function. A route maps what you type in the browser (the url) to a Python function.

>@app.route('/')<br/>
     def index():

The function should return something to the web browser,
>return 'Hello World!'

Thus our final code for our Hello world app in Flask can be as 
>from flask import Flask<br/>
>app = Flask(__name__)<br/>
><br/>
>@app.route("/")<br/>
>def index():<br/>
>&emsp; return "Hello World !"<br/>
><br/>
><br/>
>if __name__ == "__main__":<br/>
>&emsp;app.run(debug=True)<br/>


Now you can simply view your app in your web browser.
After running the program you will get a url like http://localhost:50/ simply enter it in your browser.
Here's your first web app using flask is ready.
