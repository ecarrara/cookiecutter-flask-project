# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users.tests.commands.create_user_test
    {{'~' * (cookiecutter.app_name|length + 36)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from {{cookiecutter.app_name}}.tests import BaseTestCase
from {{cookiecutter.app_name}}.modules.users.commands import CreateUserCommand
from {{cookiecutter.app_name}}.modules.users.models import User


class CreateUserCommandTest(BaseTestCase):

    def test_create_users(self):

        command = CreateUserCommand()
        command.run(name='Test', email='test@example.com', password='test123',
                    role='admin')

        users = User.query.filter(User.name == 'Test').first()
        self.assertIsNotNone(users)
        self.assertTrue(users.is_active())
