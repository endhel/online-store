from flask import render_template, session, request, url_for
from store import app, db


@app.route('/')
def home():
    return "Seja bem-vindo ao InfoStore"
