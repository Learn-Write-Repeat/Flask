from flask import Flask, session
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sender@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# lets assume all emails are in list of all_emails


from threading import Thread

# create function which will be excuted in threads

def send_email_thread(msg):
    with app.app_context():
        mail.send(msg)

with app.app_context():
    emails = ['user1@gmail.com','user2@gmail.com', 'user3@gmail.com']
    for email in emails:        
        message = 'Hello subscribers. Thanks for using our service!'
        subject = "Mr./Miss Subscriber"
        msg = Message(recipients=[email],sender = 'Sender<sender@gmail.com>',\
                          body=message,subject=subject)
        thr = Thread(target=send_email_thread, args=[msg])
        thr.start()