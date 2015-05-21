# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users.tests.logins
    {{'~' * (cookiecutter.app_name|length + 28)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import url_for
from flask_login import current_user
from {{cookiecutter.app_name}}.tests import BaseTestCase
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.modules.users.models import User


class LoginViewTestCase(BaseTestCase):

    def setUp(self):
        super(LoginViewTestCase, self).setUp()
        self.url = url_for('users.login')

    def test_render_form(self):
        response = self.client.get(self.url)
        self.assert200(response)

    def test_invalid_email(self):
        response = self.client.post(self.url, data={
            'email': 'invalid.email',
            'password': 'test123'
        })

        self.assert200(response)

        form = self.get_context_variable('form')
        self.assertEquals(len(form.email.errors), 1)

    def test_invalid_password(self):
        user = User(name='Test', email='test@example.com', password='test123',
                    role='user', active=True)

        db.session.add(user)
        db.session.commit()

        with self.client:
            response = self.client.post(self.url, data={
                'email': 'test@example.com',
                'password': 'test124'
            })

            self.assert200(response)
            self.assertIn('The e-mail address or password is invalid.',
                          response.data)

    def test_valid_login(self):
        user = User(name='Test', email='test@example.com', password='test123',
                    role='user', active=True)

        db.session.add(user)
        db.session.commit()

        with self.client:
            response = self.client.post(self.url, data={
                'email': 'test@example.com',
                'password': 'test123'
            })

            self.assertRedirects(response, '/')
            self.assertTrue(current_user.is_active())
            self.assertTrue(current_user.is_authenticated())
            self.assertFalse(current_user.is_anonymous())
