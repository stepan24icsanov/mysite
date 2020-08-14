from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'stepan24icsanov'
DATABASE = '/templates/posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from app.admin import admin
app.register_blueprint(admin)
from app.articles import arti
app.register_blueprint(arti)

from app import routes










