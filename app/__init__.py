from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'curry30'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = ' 691a46a47da22a'
app.config['MAIL_PASSWORD'] = 'a57f3f9c356fa0'

mail = Mail(app)
from app import views