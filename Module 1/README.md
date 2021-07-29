# TEMPLATES IN FLASK:

## Jinja2 :
* Jinja2 is a Python library that you can use to construct templates for various output formats from a core template text file. 
* It can be used to create HTML templates. 
* It has a rich API, and large array of syntactic directives (statements, expressions, variables, tags) that allow the dynamic injection of content into the templated file.

## Templates in Flask:
*Templates are files that contain static data as well as placeholders for dynamic data. In simple language, templates are generally the blueprints of the html code that we're going to use in webpage, which will get rendered with data to produce a final document.

## Operations on Templates:

* Template rendering:
Template rendering can be done using 
*render_template* function from the flask template package. It generates output from a template. We provide the name of the template and the variables we want to pass to the template engine as keyword arguments.
E.g., in our code we used,
 ```python
	return render_template('index.html', author='Swarada',Learning_flow= Learning_flow)
 ```

* Template Inheritance:
Templates ususally contains HTML skeleton, within blocks with the syntax:
 ```flask
{% block body %}
 <!--CODE GOES HERE-->
{% endblock %}
  ```
The above block can be replaced by a block of the same name (body) in a child template. 

* Control Structure in Flask:
We know that is a block of programming that analyses variables and chooses its next step. Here we have used control structures using 'if'. Syntax: 
  ```flask
{% if condition %}
<!--Body-->
{% endif %}
  ```

* Loops in flask:
Here, we have used 'for' loop, whose syntax is exact same as we normally use in python, except it is written within the block. Syntax:
  ```flask
{% for i in range(0,len)%}
<!--body of the loop-->
{% endfor %}
  ```
