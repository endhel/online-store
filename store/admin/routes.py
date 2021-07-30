from flask import render_template, session, request, url_for, flash, redirect
from store import app, db, bcrypt
from .form import RegistrationForm, LoginForm
from .models import User
import os


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))
    return render_template('admin/index.html', title='Admin Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        
        db.session.add(user)
        db.session.commit()

        flash(f'Usuário {form.name.data} registrado com sucesso!', 'success')

        return redirect(url_for('login'))
        
    return render_template('admin/register.html', form=form, title='Página de Registro')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Seja bem vindo, {form.email.data}!', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Não foi possível logar no sistema!')
    return render_template('admin/login.html', form=form, title='Página de Login')