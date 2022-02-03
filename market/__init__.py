from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '80880ac43be83448ab984e22'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from market import routes


