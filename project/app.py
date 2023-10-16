from flask import Flask, render_template, request, current_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_mail import Mail, Message
import os
import smtplib

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'fyjvgybny26@gmail.com'
app.config['MAIL_PASSWORD'] = 'gect heme jtdp oeoj'

mail = Mail(app)

def send_email(name, email, message):
    smtp_server = current_app.config['MAIL_SERVER']
    smtp_port = current_app.config['MAIL_PORT']
    smtp_username = current_app.config['MAIL_USERNAME']
    smtp_password = current_app.config['MAIL_PASSWORD']

    recipient_email = 'semiloreoluwaseyi20@gmail.com'
    subject = 'New Form Submission'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient_email
    msg['Subject'] = subject

    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient_email, msg.as_string())
        server.quit()
    except Exception as e:
        # Handle exceptions (e.g., log the error or provide an error message to the user)
        print(f"An error occurred: {e}")

@app.route('/', strict_slashes=False)
def home():
    # return home page.
    title = 'Home'
    return render_template('home.html')

@app.route('/about', strict_slashes=False)
def about():
    # return about page.
    title = 'About'
    return render_template('about.html')

@app.route('/services', strict_slashes=False)
def services():
    # return services page.
    title = 'Services'
    return render_template('services.html')

@app.route('/contact', strict_slashes=False, methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        message = request.form.get('Message')

        # Send an email with the form data
        send_email(name, email, message)
    # return contact page.
    title = 'Contact'
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
