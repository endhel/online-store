from flask import render_template, session, request, url_for, flash, redirect
from store import app, db
from .form import RegistrationForm


@app.route('/')
def home():
    return "Seja bem-vindo ao InfoStore"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #db_session.add(user)
        flash('Registrado com sucesso!')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Página de Registro')