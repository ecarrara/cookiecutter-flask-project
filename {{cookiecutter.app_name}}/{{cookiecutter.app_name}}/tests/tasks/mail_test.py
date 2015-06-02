# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.tests.tasks.mail
    {{'~' * (cookiecutter.project_name|length + 16)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from {{cookiecutter.app_name}}.tests import BaseTestCase
from {{cookiecutter.app_name}}.tasks.mail import send_mail
from {{cookiecutter.app_name}}.extensions import mail


class MailTestTestCase(BaseTestCase):

    def test_send_mail(self):
        with mail.record_messages() as outbox:
            send_mail(['test@example.com'], 'Test subject', 'Test message.')

            self.assertEquals(len(outbox), 1)
            self.assertEquals(outbox[0].subject, 'Test subject')
            self.assertEquals(outbox[0].message, 'Test message')
