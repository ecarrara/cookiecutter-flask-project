# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.tasks.mail
    {{'~' * (cookiecutter.project_name|length + 10)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import current_app
from flask_mail import Message
from {{cookiecutter.app_name}}.tasks import celery
from {{cookiecutter.app_name}}.extensions import mail


@celery.task
def send_mail(recipients, subject, plain, html=None, sender=None):
    if sender is None:
        sender = current_app.config.get('DEFAULT_MAIL_SENDER')

    msg = Message(subject, body=plain, html=html,
                  sender=sender, recipients=recipients)
    mail.send(msg)
