from flask import render_template

from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/info/')
def showLinks():
    return render_template('info.html')
