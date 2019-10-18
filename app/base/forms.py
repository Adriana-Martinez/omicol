from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms.fields.html5 import DateField, EmailField


## login and registration


class LoginForm(FlaskForm):
    username = TextField('Usuario', id='username_login')
    password = PasswordField('Contraseña', id='pwd_login')


class CreateAccountForm(FlaskForm):
	nombre = TextField('Nombres', validators=[DataRequired()])
	apellido = TextField('Apellidos', validators=[DataRequired()])
	tipoDocumento=  SelectField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
										('Cédula de Extranjería', 'Cédula de Extranjería'), 
										('Pasaporte', 'Pasaporte')], validators=[DataRequired()])
	documento = IntegerField('Número Documento', validators=[DataRequired()])
	fechaNacimiento = DateField('Fecha Nacimiento', validators=[DataRequired()], format = '%d/%m/%y')
	telefono = IntegerField('Teléfono', validators=[DataRequired()])
	rol = SelectField(choices=[('Administrador', 'Administrador'),
										('Coordinador', 'Coordinador'), 
										('Gestor', 'Gestor')], validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired(), Email()])
	status = SelectField(choices=[('Activo', 'Activo'),
										('Inactivo', 'Inactivo'),], validators=[DataRequired()])
	username = TextField('Usuario', id='username_create', validators=[DataRequired()])
	password = PasswordField('Contraseña', id='pwd_create', validators=[DataRequired()])
	confirm = PasswordField ( 'Confirmar Contraseña', validators=[DataRequired(),
							EqualTo('password', message = 'Password Correcto' )])