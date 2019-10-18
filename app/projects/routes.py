from flask import render_template
from flask_login import login_required
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user)

from app import db, login_manager
from app.projects import blueprint
from app.home.forms import CreateUserForm
from app.base.models import User



@blueprint.route('/projects')
@login_required
def route_default():
    return redirect(url_for('projects_blueprint.projects'))

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


@blueprint.route('/edit/<int:list_user>', methods=['GET', 'POST'])
def update_users(id):

        if request.method == 'POST':
            nombre = request.form["nombre"]
            email = request.form["email"]

            update_id = User.query.get(id)
            update_id.nombre = nombre
            update_id.email = email
            db_session.commit()

            return redirect(url_for('/users.update-modal-sm'))
        else:
            new_id = User.query.get(id)
            new_id.nombre = new_id.nombre
            new_id.apellido = new_id.apellido          
            new_id.email = new_id.email

            return render_template('users.html', data=new_id)