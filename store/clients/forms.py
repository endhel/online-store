from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, PasswordField, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm
from .models import Client


class RegistrationForm(FlaskForm):
    name = StringField('Nome: ')
    username = StringField('Nome de usuário: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.DataRequired()])
    password = PasswordField('Senha: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='As duas senhas devem ser iguais!')
    ])
    confirm = PasswordField('Redigite sua senha: ', [validators.DataRequired()])
    country = StringField('País: ', [validators.DataRequired()])
    state = StringField('Estado: ', [validators.DataRequired()])
    city = StringField('Cidade: ', [validators.DataRequired()])
    contact = StringField('Contato: ', [validators.DataRequired()])
    address = StringField('Endereço: ', [validators.DataRequired()])
    zipcode = StringField('Caixa-Postal: ', [validators.DataRequired()])
    profile = FileField('Foto de Perfil: ', validators=[
                        FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    submit = SubmitField('Cadastrar-se')

    def validate_username(self, username):
        if Client.query.filter_by(username=username.data).first():
            raise ValidationError("Este usuário já existe!")

    def validate_email(self, email):
        if Client.query.filter_by(email=email.data).first():
            raise ValidationError("Este email já foi cadastrado por outro usuário!")

class LoginForm(FlaskForm):
    email = StringField('Email: ', [validators.DataRequired()])
    password = PasswordField('Senha: ', [validators.DataRequired()])