# Topic 5: EMAIL SUPPORT IN FLASK

## Overview
Many types of applications need to notify users when certain events occur, and the
usual method of communication is email. So, here we are going to learn how to use Email support with *Flask-mail*. Before implementation, you need to install 'Flask-Mail': 
> pip install flask-mail

## Flask-Mail Configuration
* This extension is responsible for connecting SMTP (Simple Mail Transfer Protocol) server and passing emails for its delivery. 
* We need to configure Flask mail for sending mails directly. Otherwise, it will get connected to the localhost at port 25, which results in unaunthenticated emails. 
* Flask is configured through standard Flask config API. 
* We can use SSL(Secure Sockets Layer) or TLS(Transport Layer Security) protocols based on our requirement. (Note: TLS is more secure and performant than SSL )
* Following is an example demonstrating configuration using **Gmail** server:
```flask
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME']= "sender_id@gmail.com"
app.config['MAIL_PASSWORD']= "Password"
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL'] = True
```

## Integration with web-app
* To avoid having to create email messages manually every time, it is a good idea to
abstract the common parts of the application’s email sending functionality into a
function.
* Hence, we use *send_message()* function to send message to specified email. 
* Firstly, we need to verify whether the requested method was 'Post' or not. If yes, then the data will be requested from the one entered in our *form*. 
```flask
if request.method=="POST":
        email= request.form['email']
        subject= request.form['subject']
        msg= request.form['message']

        message= Message(subject, sender="sender@gmail.com", recipients=[email])
        #insert msg as message body
        message.body= msg
        mail.send(message)
```
* You can even provide an attachment as per following syntax:
```flask
#Load attachment
        with app.open_resource('Thank you.pdf') as fp:
        #attach("File name", "Type", read file)
            message.attach("Thank you.pdf", 'application/octet-stream', fp.read())
```
* To render email bodies with jinja2 templates for added functionality, we return *render_template()* method at the end.

## Sending asynchronous Mails
* The above approach sends the mail, but it also slows down the processes, as it runs in the main function.
* In case, there are a lots of emails, then your system remains engaged for a longer duration, which is quite a time consuming process. 
* Hence, we need to use asynchronous approach, using : Threads or Celery configuration. Here, we will know about implementation using Threads. 
```flask
from threading import Thread
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)

with app.app_context():
    emails = ['user1@gmail.com','user2@gmail.com', 'user3@gmail.com']
    for email in emails:        
        message = 'abcd'
        subject = 'xyz'
        msg = Message(recipients=[email],sender = 'sender@gmail.com',\
                          body=message,subject=subject)
        thr = Thread(target=send_email_thread, args=[msg])
        thr.start()
```