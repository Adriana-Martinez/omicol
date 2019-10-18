from bcrypt import gensalt, hashpw
from flask_login import UserMixin
from sqlalchemy import  Column, Integer, String, Date, DateTime
from flask import render_template
from datetime import datetime

from app import db, login_manager


class Group(db.Model, UserMixin):

	__table_args__ = {"schema":"grupos"}
	__tablename__ = 'app'

	id = Column(Integer, primary_key=True)
	nombre = Column(String)
	
	createDate = Column(DateTime, default=datetime.now())

	def __repr__(self):
		return '<Group %r>' % (self.nombre)    


@login_manager.user_loader
def user_loader(id):
	return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
	username = request.form.get('username')
	user = User.query.filter_by(username=username).first()
	return user if user else None