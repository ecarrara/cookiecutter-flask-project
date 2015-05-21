# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users
    {{'~' * (cookiecutter.app_name|length + 14)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import Blueprint, flash, redirect, render_template
from flask_babel import gettext as _
from flask_login import login_user
from {{cookiecutter.app_name}}.extensions import login_manager
from {{cookiecutter.app_name}}.modules.users.models import User
from {{cookiecutter.app_name}}.modules.users.forms import LoginForm

users = Blueprint('users', __name__, template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

            return redirect('/')

        flash(_('The e-mail address or password is invalid.'), 'warning')

    return render_template('users/login.html', form=form)
