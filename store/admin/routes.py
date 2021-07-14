from flask import render_template, session, request, url_for
from store import app, db


@app.route('/')
def home():
    return "Seja bem-vindo ao InfoStore"

@app.route('/register')
def register():
    return render_template('admin/register.html', title='Register user')