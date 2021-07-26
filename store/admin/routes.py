from flask import render_template, session, request, url_for, flash, redirect
from store import app, db, bcrypt
from .form import RegistrationForm
from .models import User
import os


@app.route('/')
def home():
    return "Seja bem-vindo ao InfoStore"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash('Registrado com sucesso!')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title='Página de Registro')