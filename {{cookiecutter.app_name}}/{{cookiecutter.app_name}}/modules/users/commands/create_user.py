# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users.commands.create_user
    {{'~' * (cookiecutter.app_name|length + 35)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask_script import Command, Option
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.modules.users.models import User


class CreateUserCommand(Command):

    option_list = (
        Option('--name', '-n', dest='name', required=True),
        Option('--email', '-e', dest='email', required=True),
        Option('--password', '-p', dest='password', required=True),
        Option('--role', '-r', dest='role', default='admin')
    )

    def run(self, name, email, password, role):
        user = User(name=name, email=email, password=password,
                    role=role, active=True)

        db.session.add(user)
        db.session.commit()
