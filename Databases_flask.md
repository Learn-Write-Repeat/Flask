# Databases using Flask

## SQL vs NoSQL Databases

A database stores application data in an organized way. The application then issues queries to retrieve specific portions of the data as they are needed. The most commonly used databases for web applications in flask are SQL and NoSQL.Here we are with some differences between them.

|                             SQL	                      |                       NoSQL                                          |
|:------------------------------------------------------|:---------------------------------------------------------------------|
|1) Databases are categorized as Relational Database    |1) NoSQL databases are categorized as Non-relational or distributed   |
|   Management System (RDBMS).	                        |   database system.                                                   |
|2)	SQL databases have fixed or static or predefined    |2) NoSQL databases have dynamic schema.                               |
|   schema.                                             |                                                                      |
|3) SQL databases display data in form of tables so it  |3) NoSQL databases display data as collection of key-value pair,      |
|    is known as table-based database.	                |   documents, graph databases or wide-column stores.                  |
|4)	SQL databases are vertically scalable.	            |4) NoSQL databases are horizontally scalable.                         | 
|5)	SQL databases use a powerful language "Structured   |5) In NoSQL databases, collection of documents are used to query the  |
|   Query Language" to define and manipulate the data.  |   data. It is also called unstructured query language.It varies from | 
|                                                       |   database to database.                                              |
|6)	SQL databases are best suited for complex queries.  |6) NoSQL databases are not so good for complex queries because these  |
|                                                       |   are not as powerful as SQL queries.                                |
|7) SQL databases are not best suited for hierarchical  |7) NoSQL databases are best suited for hierarchical data storage.     | 
|   data storage.	                                      |                                                                      |
|8)	MySQL, Oracle, Sqlite, PostgreSQL and MS-SQL etc.   |8) MongoDB, BigTable, Redis, RavenDB, Cassandra, Hbase, Neo4j, CouchDB| 
|   are the example of SQL database.	                  |   etc. are the example of nosql database.                            |

## Database Management with Flask-SQLAlchemy

Flask-SQLAlchemy is a Flask extension that simplifies the use of SQLAlchemy inside Flask applications. SQLAlchemy is a powerful relational database framework that supports several database backends. It offers a high-level ORM and low-level access to the database’s native SQL functionality.
Like most other extensions, Flask-SQLAlchemy is installed with pip:
>(venv) $ pip install flask-sqlalchemy<br/>
In Flask-SQLAlchemy, a database is specified as a URL.Here's the format ofthe URLs for the three most popular database engines.

|Database engine                   |URL                                               |
|:---------------------------------|:-------------------------------------------------|
|MySQL                             |mysql://username:password@hostname/database       | 
|Postgres                          |postgresql://username:password@hostname/database  |
|SQLite (Linux, macOS)             |sqlite:////absolute/path/to/database              | 
|SQLite (Windows)                  |sqlite:///c:/absolute/path/to/database            |

In these URLs, hostname refers to the server that hosts the database service, which could be localhost or a remote server. Database servers can host several databases, so database indicates the name of the database to use. For databases that need authentication, username and password are the database user credentials.
_SQLite databases do not have a server, so hostname, username, and password are omitted and database is the filename on disk for thedatabase._
The URL of the application database must be configured as the key SQLALCHEMY_DATABASE_URI in the Flask configuration object. The Flask-SQLAlchemy documentation also suggests setting key SQLALCHEMY_TRACK_MODIFICATIONS to Falseto use less memory unless signals for object changes are needed. Consult the Flask-SQLAlchemy documentation for information on other configuration options.
Here's the example of hello.py: database configuration to show how to initialize and configure a simple SQLite database.

>import os<br/>
>from flask_sqlalchemy import SQLAlchemy<br/>

>basedir = os.path.abspath(os.path.dirname(__file__))<br/>
>app = Flask(__name__)<br/>
>app.config['SQLALCHEMY_DATABASE_URI'] =\ <br/>
>&emsp;'sqlite:///' + os.path.join(basedir, 'data.sqlite')<br/>
>app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False<br/>
>db = SQLAlchemy(app)<br/>

The db object instantiated from the class SQLAlchemy represents the database and
provides access to all the functionality of Flask-SQLAlchemy

## Model and Relationships

### =>Models
The term model is used when referring to the persistent entities used by the application. In the context of an ORM, a model is typically a Python class with attributes thatmatch the columns of a corresponding database table.The database instance from Flask-SQLAlchemy provides a base class for models aswell as a set of helper classes and functions that are used to define their structure. 
Example of hello.py: Role and User model definition
>class Role(db.Model):
>&emsp; __tablename__ = 'roles'<br/>
>&emsp;id = db.Column(db.Integer, primary_key=True)<br/>
>&emsp;name = db.Column(db.String(64), unique=True)<br/>
>&emsp;def __repr__(self):<br/>
>&emsp; &emsp;return '<Role %r>' % self.name<br/>
>class User(db.Model):<br/>
>&emsp; &emsp; __tablename__ = 'users'<br/>
>&emsp;id = db.Column(db.Integer, primary_key=True)<br/>
>&emsp;username = db.Column(db.String(64), unique=True, index=True)<br/>
>&emsp;def __repr__(self):<br/>
>&emsp; &emsp;return '<User %r>' % self.username<br/>
The __tablename__ class variable defines the name of the table in the database. Flask-SQLAlchemy assigns a default table name if __tablename__ is omitted, but those default names do not follow the popular convention of using plurals for table names,so it is best to name tables explicitly. The remaining class variables are the attributesof the model, defined as instances of the db.Column class.

### =>Relationships
Relational databases establish connections between rows in different tables through the use of relationships.A one-to-many relationship from roles to users, because one role can belong to many users, but each user can have only one
role.
Below example shows how the one-to-many relationship is represented inthe model classes.
Ex-hello.py: relationships in the database models
>class Role(db.Model):
>&emsp; # ...
>&emsp;users = db.relationship('User', backref='role')
>class User(db.Model):
>&emsp;# ...
>&emsp;role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

A relationship connects two rows through the use of a foreignkey. The role_id column added to the User model is defined as a foreign key, and that establishes the relationship. The 'roles.id' argument to db.ForeignKey() specifies that the column should be interpreted as having id values from rows in the roles table.

The users attribute added to the model Role represents the object-oriented view of the relationship, as seen from the“one” side. Given an instance of class Role, the users attribute will return the list of users associated with that role (i.e., the “many” side). The first argument to db.relationship() indicates what model is on the other side of the relationship. The model class can be provided as a string if the class is defined later in the module.The backref argument to db.relationship() defines the reverse direction of the relationship, by adding a role attribute to the User model. This attribute can be used on any instance of User instead of the role_id foreign key to access the Role model as an object.

In most cases db.relationship() can locate the relationship’s foreign key on its own, but sometimes it cannot determine what column to use as a foreign key. For example, if the User model had two or more columns defined as Role foreign keys, then SQLAlchemy would not know which one of the two to use. Whenever the foreign key configuration is ambiguous additional arguments to db.relationship() need to be given.

## Crude Operations
CRUD operations are basically Create/Retrieve/Update or Delete operations.And a web application that deals with CRUD operations is known as a CRUD application. A typical example of a CRUD application is a Blog Website.


|Operation                         |Function                                          |
|:---------------------------------|:-------------------------------------------------|
|Create                            |Create and add new data into the Database         | 
|Retrieve                          |Retrieve data from the Database                   |
|Update                            |Update existing data into the Database            | 
|Delete                            |Delete an existing data into the Database         |


### Creating a Flask CRUD Application
We will create a simple Flask CRUD application.
Here in tne below example we will Create / Retrieve / Update / Delete Employee Information.

Therefore in this application, you can:

*Create a new Employee Information
*See the list of Employees.
*See information of a specific Employee.
*Update the Information of an Employee
*Delete an Employee information

***=> Coding the Models.py***
Here, we will use Flask_SQLAlchemy and SQLite DB.

First install Flask_SQLAlchemy
>pip install flask_sqlalchemy <br/>

Now create a models.py file and add the following code:

![image1](https://user-images.githubusercontent.com/84977514/128624961-17b31671-50b3-4245-b6ee-1b77537f1972.png)

Here we are just creating the EmployeeModel. Do check out the SQLAlchemy tutorial if you have any difficulty understanding the syntax

***=> Coding the main Application***
Now, lets code our main Flask Application File. We’ll begin by importing Flask, initialize the flask app, and set up the application runtime details.

![Screenshot (92)](https://user-images.githubusercontent.com/84977514/128625026-aecedbaa-014b-447a-861b-9aeb1cf9a3f2.png)

Now we need to link SQLite DB with SQLAlchemy. So add the following code snippet:

![Screenshot (93)](https://user-images.githubusercontent.com/84977514/128625116-70b44508-c0e9-4bb6-bebd-140a4be8054b.png)

Replace <db_name> with the name you want for your DB File.

Also, we need to link the db instance (from models.py) and create DB file before the user accesses the server. So for that:

![Screenshot (94)](https://user-images.githubusercontent.com/84977514/128625212-5ab59bda-0269-4065-b43a-53476fde8569.png)

Okay, now that the DB and models are in place, lets code our CRUD views.

#### 1. Coding the Create view
The Create view should be able to do the following:

When the Client goes to this page (GET method), it should display a Form to get the Client’s Data.
On Submission (POST method), it should save the Client’s data in the EmployeeModel Database.
So the Create View will be:

![Screenshot (95)](https://user-images.githubusercontent.com/84977514/128625266-11c55d02-1aa1-410d-b1ee-fb1b0cd9fe5f.png)

The createpage.html will contain the HTML Form:

![Screenshot (96)](https://user-images.githubusercontent.com/84977514/128625352-c4efa29e-9050-45fe-9767-e15ffc41722f.png)

#### 2. Coding the Retrieve views
Here we will have 2 views:


-To display the list of Employees. <br/>
-To display the information of a single Employee.

So the First RetrieveDataList view will be:

![Screenshot (97)](https://user-images.githubusercontent.com/84977514/128625409-bf6a457f-b596-49b8-a653-c00b2f830a67.png)

The datalist.html file will display the list of Employees:

![Screenshot (98)](https://user-images.githubusercontent.com/84977514/128625536-81828a5d-256b-43b3-93ac-8568cdcfbc08.png)


And the Second RetrieveSingleEmployee View will be:

![Screenshot (99)](https://user-images.githubusercontent.com/84977514/128625749-35f0a831-5cb0-4776-b7fa-f8e19489d11b.png)

EmployeeModel.query.filter_by(employee_id = id).first() will return the first Employee with Employee ID = id in the DB or return None if the Employee with that id does not exist.


The data.html displays the information of the Employee:

![Screenshot (100)](https://user-images.githubusercontent.com/84977514/128625754-5755d7d1-7bbe-4e84-971d-ccb9cd7618ee.png)

#### 3. Coding the Update View
The Update View will update the Employee details in the DB with the new one submitted by the user.

Hence the Update View will be:

![Screenshot (101)](https://user-images.githubusercontent.com/84977514/128625764-c310dfbd-2091-4090-9870-9b4c49ecf169.png)

The user will submit the new details via the Form. Here we first delete the old information present in the DB and then add the new information

The update.html displays the Form for the submission of new details:

![Screenshot (102)](https://user-images.githubusercontent.com/84977514/128625772-2455bdff-1c97-4ea0-90df-9cc5d02e1d49.png)

#### 4. Coding the Delete View
The Delete View will just delete the Employee Information from the DB File.

The Delete View will be:

![Screenshot (103)](https://user-images.githubusercontent.com/84977514/128625782-425733fb-bbc8-438c-ac30-730207dc4859.png)

The delete.html just re-confirms the deletion:

![Screenshot (104)](https://user-images.githubusercontent.com/84977514/128625787-e20cf277-c56a-45d2-a4d3-20f202572eeb.png)

If the user presses Yes then the Employee is deleted. Or else he is taken back.

Now you have successfully created a web application using Flask CRUD operations.

## Database Migrations using Flask-Migrate

Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are provided as command-line arguments under the flask db command.

#### =>Installation
Install Flask-Migrate with pip:

>pip install Flask-Migrate <br/>

#### =>Example 
This is an example application that handles database migrations through Flask-Migrate:

>from flask import Flask<br/>
>from flask_sqlalchemy import SQLAlchemy<br/>
>from flask_migrate import Migrate<br/>
><br/>
>app = Flask(__name__)<br/>
>app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'<br/>
><br/>
>db = SQLAlchemy(app)<br/>
>migrate = Migrate(app, db)<br/>
><br/>
>class User(db.Model):<br/>
>&emsp;id = db.Column(db.Integer, primary_key=True)<br/>
>&emsp;name = db.Column(db.String(128))<br/>

With the above application you can create the database or enable migrations if the database already exists with the following command:

>$ flask db init<br/>

Note that the FLASK_APP environment variable must be set according to the Flask documentation for this command to work. This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.

You can then generate an initial migration:

>$ flask db migrate<br/>

The migration script needs to be reviewed and edited, as Alembic currently does not detect every change you make to your models. In particular, Alembic is currently unable to detect indexes. Once finalized, the migration script also needs to be added to version control.

Then you can apply the migration to the database:

>$ flask db upgrade<br/>

Then each time the database models change repeat the migrate and upgrade commands.

To sync the database in another system just refresh the migrations folder from source control and run the upgrade command.

To see all the commands that are available run this command:

>$ flask db --help<br/>


Thus, Now we are clear with the concept of Databases using Flask. 
