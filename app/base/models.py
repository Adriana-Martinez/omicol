from bcrypt import gensalt, hashpw
from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Date, BigInteger, DateTime
from flask import render_template
from datetime import datetime

from app import db, login_manager


class User(db.Model, UserMixin):

	__table_args__ = {"schema":"usuarios"}
	__tablename__ = 'usuarios'

	id = Column(Integer, primary_key=True)
	nombre = Column(String)
	apellido = Column(String)
	tipoDocumento = Column(String)
	documento = Column(BigInteger, unique=True)
	fechaNacimiento = Column(Date)
	telefono = Column(BigInteger)
	rol = Column(String)
	email = Column(String)
	status = Column(String)
	username = Column(String, unique=True)
	password = Column(Binary)
	dateCreate = Column(DateTime, default=datetime.now())

	def __init__(self, **kwargs):
		for property, value in kwargs.items():
			# depending on whether value is an iterable or not, we must
			# unpack it's value (when **kwargs is request.form, some values
			# will be a 1-element list)
			if hasattr(value, '__iter__') and not isinstance(value, str):
				# the ,= unpack of a singleton fails PEP8 (travis flake8 test)
				value = value[0]
			if property == 'password':
				value = hashpw(value.encode('utf8'), gensalt())
			setattr(self, property, value)

	def __repr__(self):
		return str(self.username)

	def __repr__(self):
		return '<User %r>' % (self.nombre)    


@login_manager.user_loader
def user_loader(id):
	return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
	username = request.form.get('username')
	user = User.query.filter_by(username=username).first()
	return user if user else None