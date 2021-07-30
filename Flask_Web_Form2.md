# 👉STEPS TO CREATE WEB_FORM:-
 ***Only follow my steps to make your first web form***
 
 1. First install flask and create a virtual environment in your system.
  I have already installed flask and created a virtual environment **"myenv"** in the folder flasky of my system.
 
 2.In your activated virtual environment, we will install our packages by typing:
 > pip install flask-wtf
 
 3.We create a basic **hello.py** file  in folder flasky which contain our Flask app,routes and forms **(Fask-WTF Configuration)**:
 <pre>
 from flask import Flask, render_template
 app = Flask(__name__)
 app.config['SECRET_KEY'] = 'hard to guess string'
 </pre>
 
 4.Let's create and add a form to our current **hello.py** file **(Form Class Definition)**:
 <pre>
 from flask_wtf import FlaskForm
 from wtforms import StringField, SubmitField
 from wtforms.validators import DataRequired
 
 class GreetUserForm(FlaskForm):
     name = StringField('Enter your name:-', validators=[DataRequired()])
     submit = SubmitField('Submit')
 </pre>
 
 5.Let's begin by creating a route to display and process our form **(Handle a web form with GET and POST request methods)**:
 <pre>
 @app.route('/', methods=['GET', 'POST'])
 def index():
     name = None
     form = GreetUserForm()
     if form.validate_on_submit():
         name = form.name.data
         form.name.data = ''
     return render_template('index.html', form=form, name=name)
 </pre>
 
 ***After step no. 3,4 and 5 our file looks like this:
 
 <img src="https://i.ibb.co/ZckGTbM/Screenshot-205.png" alt="Screenshot-205" border="0">
 
 6.To see the form, we need to create the **index.html** under template folder. Create the file and add the following code to it:
 <pre>
 &lt;!DOCTYPE html&gt;
 &lt;html lang="en"&gt;
 &lt;head&gt;
     &lt;meta charset="UTF-8"&gt;
     &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
     &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
     &lt;title&gt;Document&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
     &lt;form method="POST"&gt;
         {{ form.hidden_tag() }}
         {{ form.name.label }} {{ form.name() }}
         {{ form.submit() }}
     &lt;/form&gt;
 &lt;/body&gt;
 &lt;/html&gt;
 </pre>
 
 7.Now, let’s go to our powershell/terminal/cmd to start our Flask app:
 ***Here i am using windows powershell to run the flask app***
 
 First activate your virtual environment and write the following code step by step to get the url for your web form:
 
 <img src="https://i.ibb.co/2MR8z6F/Screenshot-209.png" alt="Screenshot-209" border="0">
 
 8.Copy the url (in the last line of your powershell) in the browser to get your first web form:
 
 <img src="https://i.ibb.co/dgtCLxQ/Screenshot-214.png" alt="Screenshot-214" border="0"> 
 ✌***Congratulations! You made your first Web Form in Flask***
 
 **do visit me** :point_down:

<a href="https://www.linkedin.com/in/shashank-a12a851a0/">
  <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://github.com/Shashankkrj"> <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
<a href="https://www.instagram.com/shashank_krj/">
  <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a href="https://m.facebook.com/">
 <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />
</a>

***thanks for reading*** :heart:
 
