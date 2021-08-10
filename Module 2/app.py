from flask import Flask, render_template, request

from flask_mail import Mail, Message

app = Flask(__name__)

#mail configuration for gmail 

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME']= "sender@gmail.com"
app.config['MAIL_PASSWORD']= "pass"
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

#define route
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    #if the requested method was post, then send the message
    if request.method=="POST":
        email= request.form['email']
        subject= request.form['subject']
        msg= request.form['message']

        message= Message(subject, sender="user@gmail.com", recipients=[email])
        #insert msg as message body
        message.body= msg

        # Load attachment
        with app.open_resource('Thank you.pdf') as fp:
        # attach("File name", "Type", read file)
            message.attach("Thank you.pdf", 'application/octet-stream', fp.read())
     
        #call send function
        mail.send(message)
        #define success message
        success= "Message sent Successfully! "

        return render_template("result.html", success=success)


if __name__ == "__main__":
    app.run(debug=True)