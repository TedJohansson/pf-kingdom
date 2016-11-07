from flask_wtf import Form
from wtforms import StringField, BooleanField


class LoginForm(Form):
    Username = StringField('Username')
    password = StringField('password')
    remember_me = BooleanField('remember_me', default=False)


class GridForm(Form):
    building_name = StringField('building_name')