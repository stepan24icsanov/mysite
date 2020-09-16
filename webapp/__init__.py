from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_socketio import SocketIO
import os


app = Flask(__name__)
app.secret_key = 'stepan24icsanov'
DATABASE = '/templates/posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
socketio = SocketIO(app)
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
