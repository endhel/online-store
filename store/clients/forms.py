from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Addclients(Form):
    name = StringField('Nome: ')
    username = StringField('Nome de usuário: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.DataRequired()])
    password = PasswordField('Senha: ', [validators.DataRequired(
    ).validators.EqualsTo('confirm', message='As duas senhas devem ser iguais!')])
    confirm = PasswordField('Redigite sua senha: ', [
                            validators.DataRequired()])
    country = StringField('País: ', [validators.DataRequired()])
    state = StringField('Estado: ', [validators.DataRequired()])
    city = StringField('Cidade: ', [validators.DataRequired()])
    contact = StringField('Contato: ', [validators.DataRequired()])
    address = StringField('Endereço: ', [validators.DataRequired()])
    zipcode = StringField('Caixa-Postal: ', [validators.DataRequired()])
    profile = StringField('Foto de Perfil: ', validators=[
                          FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'Apenas fotos'])

    submit = SubmitField('Cadastrar')
