from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    Username = StringField('Username')
    password = StringField('password')
    remember_me = BooleanField('remember_me', default=False)