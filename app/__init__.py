from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Karraine'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'c08dcf01b86990'
app.config['MAIL_PASSWORD'] = '3332240b2f84ec'
mail = Mail(app)
from app import views