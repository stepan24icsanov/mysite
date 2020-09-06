from flask import render_template, jsonify
from webapp import app
import datetime

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stepan')
def stepan():
    return jsonify({'stepan': 'stepan'})

