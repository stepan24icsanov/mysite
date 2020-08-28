from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment


app = Flask(__name__)
app.secret_key = 'stepan24icsanov'
DATABASE = '/templates/posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
moment = Moment(app)
from webapp.admin import admin

app.register_blueprint(admin)
from webapp.articles import arti

app.register_blueprint(arti)

from webapp import routes
from webapp.auth import login_manager
from webapp.models import *
import webapp.auth.auth_routes
