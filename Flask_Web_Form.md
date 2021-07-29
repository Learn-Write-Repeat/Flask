# 👉WEB FORMS
 
 When you hear about form, what comes in your mind? 

<pre><img src="https://i.ibb.co/jy9yFjd/javascript-validation-with-html-form-1.png" alt="javascript-validation-with-html-form-1" border="0" width="330" height="330"><img src="https://i.ibb.co/nf8tZFX/student-form.jpg" alt="student-form" border="50" width="330" height="330" margin="5px"><img src="https://i.ibb.co/wSBgt4z/images.png" alt="images" border="0" width="330" height="330" margin="5px"></pre>

Literally one of the above.                                                                                                                                            
We all see lots of forms in our daily life. Some of them are offline and some are online. But in this topic, we are talking about **WEB FORM** which is a online type of form.

## 👍Introduction to FORM

**Forms are used to collect the required information in a logical, meaningful fashion for communication and pass to another entity.**

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


|Field type                         | Description                                                         |
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
