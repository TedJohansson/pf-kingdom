import os
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import basedir
from flask_sqlalchemy import SQLAlchemy

lm = LoginManager()
kingdom = Flask(__name__)
kingdom.config.from_object('config')
db = SQLAlchemy(kingdom)
bcrypt = Bcrypt(kingdom)
lm.init_app(kingdom)
lm.login_view = 'login'
bcrypt = Bcrypt(kingdom)

from kingdom import views, models