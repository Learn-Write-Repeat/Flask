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
* **Creating an API Blueprint:**
* 

