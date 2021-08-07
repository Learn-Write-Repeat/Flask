# 🔥Application Programming Interfaces

Let us understand API with an example:-                                                                                                                        
**Example 1:-** When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, 
performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. 
This is what an API is - all of this happens via API.

**Example2:-** Imagine you’re sitting at a table in a restaurant with a menu of choices to order from. The kitchen is the part of the “system” that will prepare your order. What is 
missing is the critical link to communicate your order to the kitchen and deliver your food back to your table. That’s where the waiter or API comes in. The waiter is the messenger
– or API – that takes your request or order and tells the kitchen – the system – what to do. Then the waiter delivers the response back to you; in this case, it is the food.

By the above two examples, we define API as follows:-                                                                                                                    
***An API is a set of defined rules that explain how computers or applications communicate with one another. APIs sit between an application and the web server, acting as an intermediary 
layer that processes data transfer between systems.***

## 🤔Introduction to REST API
**RE**presentational **S**tate **T**ransfer (REST) is an architectural style that defines a set of constraints to be used for creating web services. REST API is a way of accessing web services in a simple and flexible way without having any processing.
REST technology is generally preferred to the more robust Simple Object Access Protocol (SOAP) technology because REST uses less bandwidth, simple and flexible making it more suitable for internet usage. It’s used to fetch or give some information from a web service. All communication done via REST API uses only HTTP request. 

<img src="https://i.ibb.co/5Bp41Th/maxresdefault.jpg" alt="maxresdefault" border="0">

#### 👉Brief explanation of REST API:                                                                                                                                    
***Representational:-*** the resource (image, page, video, profile) is represented by the web server to the client in any format like HTML, Image, JSON, XML etc.

***State:-*** the state of the application (web site) on a client's computer changes as the client clicks from one link to the next. Ask the client clicks on the link, they request additional resources, and the application "state" changes.

***Transfer-*** the transfer of resources from the web server to the client in a "representational" state which can be read by the client or implemented in the application program by the programmer. The transfer may also refer to the application state transfer as the client browses a web site.

***API:-*** application programming interface provides useful methods/functions which a programmer can implement into his own application in a chosen programming language like PHP. The API makes it easy for programmers to implement. It's important to note that the response we get when sending REST API request will usually be in JSON, XML or other format which makes it easy to implement in the code and it's not meant to be read immediately by a human being.

#### 👉***Roy Fielding’s <a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm" target="-blank">PhD dissertation</a>*** describes the REST architectural style for web services in terms of its six defining characteristics:
***Client–server:-*** There must be a clear separation between clients and servers.

***Stateless:-*** A client request must contain all the information that is necessary to carry it out.The server must not store any state about the client that persists from one request to the next.

***Cache:-*** Responses from the server can be labeled as cacheable or noncacheable so that clients (or intermediaries between clients and servers) can use a cache for optimization purposes.

***Uniform interface:-*** The protocol by which clients access server resources must be consistent, well defined, and standardized. This is the most complex aspect of REST, covering the use of unique resource identifiers, resource representations, self-descriptive messages between client and server, and hypermedia.

***Layered system:-*** Proxy servers, caches, or gateways can be inserted between clients and servers as necessary to improve performance, reliability, and scalability.

***Code-on-demand:-*** Clients can optionally download code from the server to execute in their context.

## 👨‍🔧RESTful Web Services with Flask
Flask makes it very easy to create RESTful web services. The familiar route() decorator along with its methods optional argument can be used to declare the routes that handle the resource URLs exposed by the service. The two formats commonly used with RESTful web services are JavaScript Object Notation (JSON) and Extensible Markup Language (XML). Working with JSON data is simple, as JSON data included with a request can be obtained in dictionary format by calling **request.get_json()**, and a response that needs to contain JSON can be easily generated from a Python dictionary using Flask’s jsonify() helper function.

The following sections show how Flasky can be extended with a RESTful web servicethat gives clients access to blog posts and related resources:
* **🎯Creating an API Blueprint:**                                                                                                                                   
Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications. Blueprints can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications. A Blueprint object works similarly to a Flask application object, but it is not actually an application. A blueprint in Flask is not a **pluggable app** because it is not actually an application – it’s a set of operations which can be registered on an application, even multiple times.                                                                                                                                
The routes associated with a RESTful API form a self-contained subset of the application, so putting them in their own blueprint is the best way to keep them well organized. The general structure of the API blueprint within the application is                                                                                                             
<pre>
 |-flasky
   |-app/
     |-api
       |-__init__.py
       |-users.py
       |-posts.py
       |-comments.py
       |-authentication.py
       |-errors.py
       |-decorators.py
</pre>
The API blueprint implements each resource in a separate module. Modules to take care of authentication and error handling and to provide custom decorators are alsoincluded. The blueprint constructor is shown below:  

***app/api/__init__.py: API blueprint creation***
<pre>
 from flask import Blueprint
 api = Blueprint('api', __name__)
 from . import authentication, posts, users, comments, errors
</pre>
The structure of the blueprint package constructor is similar to that of the other blueprints. Importing all the components of the blueprint is necessary so that routes and
other handlers are registered. Since many of these modules need to import the api blueprint referenced here, the imports are done at the bottom to help prevent errors due to circular dependencies.
The registration of the API blueprint is shown below:

***app/init.py: API blueprint registration***
<pre>
 def create_app(config_name):
     # ...
     from .api import api as api_blueprint
     app.register_blueprint(api_blueprint, url_prefix='/api/v1')
     # ...
</pre>
The API blueprint is registered with a URL prefix, so that all its routes will have their URLs prefixed with /api/v1. Adding a prefix when registering the blueprint is a good
idea because it eliminates the need to hardcode the version number in every blueprint route.

* **❌Error Handling:**                                                                                                                                         
A RESTful web service informs the client of the status of a request by sending the appropriate HTTP status code in the response, plus any additional information in the response body.                                                                                                                                                     
***Some of the HTTP response status codes typically returned by APIs are:***

|HTTP status code | Name                  | Description                                                                                     |
|-----------------|-----------------------|-------------------------------------------------------------------------------------------------|
|200              | OK                    | The request was completed successfully.                                                         |
|201              | Created               | The request was completed successfully and a new resource was created as a result.              |
|202              | Accepted              | The request was accepted for processing, but it is still in progress and will run synchronously.|
|204              | No Content            | The request was completed successfully and there is no data to return in the response.          |
|400              | Bad Request           | The request is invalid or inconsistent.                                                         |
|401              | Unauthorized          | The request does not include authentication information or the credentials provided are invalid.|
|403              | Forbidden             | The authentication credentials sent with the request are insufficient for the request.          |
|404              | Not Found             | The resource referenced in the URL was not found.                                               |
|405              | Method Not Allowed    | The method requested is not supported for the given resource.                                   |
|500              | Internal Server Error | An unexpected error occurred while processing the request.                                      |

The handling of status codes 404 and 500 presents a small complication, in that these errors are normally generated by Flask on its own, and will return an HTML response. This can confuse an API client, which will likely expect all responses in JSON format. One way to generate appropriate responses for all clients is to make the error handlers adapt their responses based on the format requested by the client, a technique called content negotiation.
Below example shows an improved 404 error handler that responds with JSON to web service clients and with HTML to others. The 500 error handler is written in a similar way.

***app/api/errors.py: 404 error handler with HTTP content negotiation***
<pre>
@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
         response = jsonify({'error': 'not found'})
         response.status_code = 404
         return response
    return render_template('404.html'), 404
</pre>

This new version of the error handler checks the Accept request header, which is decoded into request.accept_mimetypes, to determine what format the client wants the response in. Browsers generally do not specify any restrictions on response formats, but API clients typically do. The JSON response is generated only for clients that include JSON in their list of accepted formats, but not HTML.

The remaining status codes are generated explicitly by the web service, so they can be implemented as helper functions inside the blueprint in the errors.py module.
Below example shows the implementation of the 403 error; the others are similar.

***app/api/errors.py: API error handler for status code 403***
<pre>
def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response
</pre>
View functions in the API blueprint can invoke these auxiliary functions to generate error responses when necessary.
