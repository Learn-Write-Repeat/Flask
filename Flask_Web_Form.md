# 👉WEB FORMS
 
 When you hear about form, what comes in your mind? 

<pre><img src="https://i.ibb.co/jy9yFjd/javascript-validation-with-html-form-1.png" alt="javascript-validation-with-html-form-1" border="0" width="330" height="330"><img src="https://i.ibb.co/nf8tZFX/student-form.jpg" alt="student-form" border="50" width="330" height="330" margin="5px"><img src="https://i.ibb.co/wSBgt4z/images.png" alt="images" border="0" width="330" height="330" margin="5px"></pre>

Literally one of the above.                                                                                                                                            
We all see lots of forms in our daily life. Some of them are offline and some are online. But in this topic, we are talking about **WEB FORM** which is a online type of form.

## 👍Introduction to FORM

***Forms are used to collect the required information in a logical, meaningful fashion for communication and pass to another entity.***

#### 🤷‍♂️WHY WE NEED WEB FORM?

As we know that templates are unidirectional, which means they allow information to flow from the server to the user. For most applications,however, there is also a need to have information that flows in the other direction,
with the user providing data that the server accepts and processes.For that we create Web Forms where users can enter information.
The form data is then submitted by the web browser to the server, typically in the form of a POST request.

The Flask request object exposes all the information sent by the client in a request and, in particular for POST requests containing form data, provides access to the user information through request.form.
Although the support provided in Flask’s request object is sufficient for the handling of web forms, there are a number of tasks that can become tedious and repetitive.
Two good examples are the generation of HTML code for the forms and the validation of the submitted form data.

## 😎Flask-WTF

Flask-WTF provides your Flask application integration with WTForms.
WTF stands for WT Forms which is intended to provide the interactive user interface for the user. The WTF is a built-in module of the flask which provides an alternative way of designing forms in the flask web applications.

To use WT Forms,we need to install Flask-WTF and its dependencies which can be done by pip installer:
<pre style="background:black">
(venv) $ pip install flask-wtf
</pre>

## ⚙️CONFIGURATION
The way Flask is designed usually requires the configuration to be available when the application starts up. You can hard code the configuration in the code, which for many small applications is not actually that bad, but there are better ways.

Independent of how you load your config, there is a config object available which holds the loaded configuration values:**The config attribute of the Flask object**. This is the place where Flask itself puts certain configuration values and also where extensions can put their configuration values. But this is also where you can have your own configuration.

Unlike most other extensions, Flask-WTF does not need to be initialized at the application level, but it expects the application to have a secret key configured. A secret key
is a string with any random and unique content that is used as an encryption or signing key to improve the security of the application in several ways. Flask uses this key
to protect the contents of the user session against tampering. You should pick a different secret key in each application that you build and make sure that this string is
not known by anyone.

By below example,we know how to configure secret key in Flask:-
<pre>
app=Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"
</pre>

Here **app.config** dictionary is a general-purpose place to store configuration variables used by Flask, extensions, or the application itself. Configuration values can be added to the app.config object using standard dictionary syntax. The configuration object also has methods to import configuration values from files or the environment. 

The **SECRET_KEY** configuration variable that I added as the only configuration item is an important part in most Flask applications. Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called ***Cross-Site Request Forgery or CSRF (pronounced "seasurf")***. As its name implies, the secret key is supposed to be secret, as the strength of the tokens and signatures generated with it depends on no person outside of the trusted maintainers of the application knowing it.

## 📋FORM CLASSES
***Form classes are Python models that determine the data our forms will capture, as well as the logic for validating whether or not a user has adequately completed a form when they attempt to submit. These classes are going to live in forms.py.***

The WTforms package contains a **Form** class, which has to be used as a parent for user- defined form.

When using Flask-WTF, each web form is represented in the server by a class that inherits from the class FlaskForm. The class defines the list of fields in the form, each
represented by an object. Each field object can have one or more validators attached. A validator is a function that checks whether the data submitted by the user is valid.
 
Let us understand this topic with an example:-
<pre>
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GreetUserForm(FlaskForm):
    username = StringField('Enter Your Name:', validators=[DataRequired()])
    submit = SubmitField('Submit')
</pre>

In the above example **GreetUserForm** class contains a **StringField**. As the name implies, this field accepts and will return a string value (you can always convert that input to other data types as the need arises). The name of the field is **username**, and we'll use this name to access data of the form element.

The **label** paremeters(i.e. 'Enter Your Name:' and 'Submit') are what will be rendered on our page so that users would understand what data a form element captures. We also have a **submit button**, which will try to submit the form if all fields pass our validation criteria i.e. **DataRequired()** (It ensures that the field is not submitted empty).

**WTforms** package contains definitions of various form fields. Some **Standard HTML fields** supported by form are listed below:-
|Field type            | Description                                                         |
|----------------------|---------------------------------------------------------------------|
|BooleanField          | Checkbox with True and False values                                 |
|DateField             | Text field that accepts a datetime.date value in a given format     |
|DateTimeField         | Text field that accepts a datetime.datetime value in a given format |
|DecimalField          | Text field that accepts a decimal.Decimal value                     |
|FileField             | File upload field                                                   |
|HiddenField           | Hidden text field                                                   |
|MultipleFileField     | Multiple file upload field                                          |
|FieldList             | List of fields of a given type                                      | 
|FloatField            | Text field that accepts a floating-point value                      |
|FormField             | Form embedded as a field in a container form                        |
|IntegerField          | Text field that accepts an integer value                            |
|PasswordField         | Password text field                                                 |
|RadioField            | List of radio buttons                                               |
|SelectField           | Drop-down list of choices                                           |
|SelectMultipleField   | Drop-down list of choices with multiple selection                   |
|SubmitField           | Form submission button                                              |
|StringField           | Text field                                                          |
|TextAreaField         | Multiple-line text field                                            |

**WTForms** package also contains validator class. It is useful in applying validation to form fields. Following list shows commonly used **validators**:-

|Validator             | Description                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------------|
|DataRequired          | Validates that the field contains data after type conversion                                              |
|Email                 | Validates an email address                                                                                |
|EqualTo               | Compares the values of two fields; useful when requesting a password to be entered twice for confirmation |
|InputRequired         | Validates that the field contains data before type conversion                                             |
|IPAddress             | Validates an IPv4 network address                                                                         |
|Length                | Validates the length of the string entered                                                                |
|MacAddress            | Validates a MAC address                                                                                   |
|NumberRange           | Validates that the value entered is within a numeric range                                                |
|Optional              | Allows empty input in the field, skipping additional validators                                           |
|Regexp                | Validates the input against a regular expression                                                          |
|URL                   | Validates a URL                                                                                           |
|UUID                  | Validates a UUID                                                                                          |
|AnyOf                 | Validates that the input is one of a list of possible values                                              |
|NoneOf                | Validates that the input is none of a list of possible values                                             |

## 😄Rendering HTML Forms
Form fields are callables that, when invoked from a template, render themselves to HTML. Assuming that the view function passes a GreetUserForm instance to the template
as an argument named form, the template can generate a simple HTML form as follows:
<pre>
&lt;form method="POST"&gt;
    {{ form.hidden_tag() }}
    {{ form.username.label }} {{ form.username() }}
    {{ form.submit() }}
&lt;/form&gt;
</pre>
Note that in addition to the username and submit fields, the form has a form.hidden_tag() element. This element defines an extra form field that is hidden, used by Flask-WTF to 
implement CSRF protection. Of course, the result of rendering a web form in this way is extremely bare. Any keyword arguments added to the calls that render the fields are converted into HTML attributes for the field—so, for example, you can give the field id or class attributes and then define CSS styles for them:
<pre>
&lt;form method="POST"&gt;
 {{ form.hidden_tag() }}
 {{ form.username.label }} {{ form.username(id='my-text-field') }}
 {{ form.submit() }}
&lt;/form&gt;
</pre>

## 💼Form Handling in View Functions
