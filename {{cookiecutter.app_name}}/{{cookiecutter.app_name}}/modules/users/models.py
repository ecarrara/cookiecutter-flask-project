# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users.models
    {{'~' * (cookiecutter.app_name|length + 21)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from {{cookiecutter.app_name}}.extensions import db


class User(db.Model):

    __tablename__ = 'users'

    ROLES = ['user', 'admin']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    role = db.Column(db.Enum(*ROLES, name='user_roles'), nullable=False,
                     server_default='user')

    def is_active(self):
        return self.active
