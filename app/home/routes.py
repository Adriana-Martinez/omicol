from flask import render_template
from flask_login import login_required
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user)
from werkzeug import secure_filename
import os

from app import db, login_manager
from app.home import blueprint
from app.home.forms import CreateUserForm, UploadForm
from app.base.models import User


@blueprint.route('/home')
@login_required
def route_default():
    return redirect(url_for('home_blueprint.users'))


@blueprint.route('/<template>')
@login_required
def route_template(template):
	return render_template(template + '.html')


@blueprint.route('/users', methods=['POST'])
def create_user():
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return jsonify('success')

@blueprint.route('/users', methods=['GET', 'POST'])
def create_users():
    create_user_form = CreateUserForm(request.form)
    list_user = User.query.all()
    if current_user.is_authenticated:
        return render_template(
            'users.html',
            create_user_form=create_user_form,
            list_user=list_user
        )
    return redirect(url_for('home_blueprint.route_default'))

@blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    form= UploadForm(request.form)
    if request.method == "POST":
        f = request.files['archive']
        filename = secure_filename(f.filename)
        f.save(os.path.join('upload/', filename))
        if current_user.is_authenticated:
            return render_template('users.html', form=form)
    return redirect(url_for('home_blueprint.route_default'))


@blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_users(id):

        if request.method == "POST":
            nombre = request.form["inputNombre"]
            apellido = request.form["inputApellido"]
            email = request.form["inputEmail"]

            update_id = User.query.get(id)
            update_id.nombre = nombre
            update_id.apellido = apellido
            update_id.email = email
            db.session.commit()

            return redirect(url_for('/users.update-modal-sm'))
        else:
            new_id = User.query.get(id)
            new_id.nombre = new_id.nombre
            new_id.apellido = new_id.apellido          
            new_id.email = new_id.email
            return render_template('users.html', data=new_id)

@blueprint.route('/groups', methods=['POST'])
def create_group():
    group = Group(**request.form)
    db.session.add(group)
    db.session.commit()

