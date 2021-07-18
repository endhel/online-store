from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo:', [validators.Length(min=4, max=25)])
    username = StringField('Nome de Usuário:', [validators.Length(min=4, max=25)])
    email = StringField('E-mail:', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha:', [
        validators.DataRequired(),
        validators.EqualTo('Confirmar sua senha:', message='As senhas devem ser iguais!')
    ])
    confirm = PasswordField('Digite sua senha novamente:')