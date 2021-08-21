from flask import redirect, render_template, url_for, flash, request, session, current_app
from store import db, app, photos
from .forms import AddClients
import secrets
import os


@app.route('/clients/register', methods=['GET', 'POST'])
def addClient():

    form = AddClients(request.form)
    return render_template('clients/register.html', form=form)
