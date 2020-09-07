from flask import render_template, jsonify, request
from flask_socketio import send
from flask_login import current_user

from webapp import app, socketio
import datetime


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@socketio.on('message')
def handle_comment(comment):
    date = datetime.datetime.utcnow()
    send([current_user.user_name, comment, f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}"], broadcast=True)
