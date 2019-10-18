from flask_wtf import FlaskForm
from wtforms import * 
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, EqualTo																														

from wtforms.ext.sqlalchemy.orm import model_form

## Create User

class CreateUserForm(FlaskForm):

	nombre = TextField('Nombres', validators=[DataRequired()])
	apellido = TextField('Apellidos', validators=[DataRequired()])
	tipoDocumento=  SelectField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
										('Cédula de Extranjería', 'Cédula de Extranjería'), 
										('Pasaporte', 'Pasaporte')], validators=[DataRequired()])
	documento = IntegerField('Documento', validators=[DataRequired(),])
	fechaNacimiento = DateField('Fecha Nacimiento', validators=[DataRequired()])
	telefono = IntegerField('Teléfono', validators=[DataRequired()])
	rol=  SelectField(choices=[('Administrador', 'Administrador'),
										('Coordinador', 'Coordinador'), 
										('Gestor', 'Gestor')], validators=[DataRequired()])
	status=  SelectField(choices=[('Activo', 'Activo'),
										('Inactivo', 'Inactivo')], validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired(), Email()])
	username = TextField('Usuario', id='username_create', validators=[DataRequired()])
	password = PasswordField('Contraseña', id='pwd_create', validators=[DataRequired()])
	confirm = PasswordField ( 'Confirmar Contraseña', validators=[DataRequired(),
							EqualTo('password', message = 'Password Correcto' )])

class UpdateUserForm(FlaskForm):

	nombre = TextField('Nombres', validators=[DataRequired()])
	apellido = TextField('Apellidos', validators=[DataRequired()])
	tipoDocumento=  SelectField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
										('Cédula de Extranjería', 'Cédula de Extranjería'), 
										('Pasaporte', 'Pasaporte')], validators=[DataRequired()])
	documento = IntegerField('Documento', validators=[DataRequired(),])
	fechaNacimiento = DateField('Fecha Nacimiento', validators=[DataRequired()])
	telefono = IntegerField('Teléfono', validators=[DataRequired()])
	rol=  SelectField(choices=[('Administrador', 'Administrador'),
										('Coordinador', 'Coordinador'), 
										('Gestor', 'Gestor')], validators=[DataRequired()])
	status=  SelectField(choices=[('Activo', 'Activo'),
										('Inactivo', 'Inactivo')], validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired(), Email()])
	username = TextField('Usuario', id='username_create', validators=[DataRequired()])
	password = PasswordField('Contraseña', id='pwd_create', validators=[DataRequired()])
	confirm = PasswordField ( 'Confirmar Contraseña', validators=[DataRequired(),
							EqualTo('password', message = 'Password Correcto' )])
	
class CreateGroupForm(FlaskForm):

	nombre = TextField('Nombre', validators=[DataRequired()])

class UploadForm(FlaskForm):
    file = FileField()