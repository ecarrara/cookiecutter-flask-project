# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users.forms
    {{'~' * (cookiecutter.app_name|length + 20)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask_wtf import Form
from flask_babel import lazy_gettext as _
from wtforms.fields import TextField, PasswordField
from wtforms.validators import InputRequired, Email


class LoginForm(Form):

    email = TextField(_(u'E-mail address'), validators=[Email()])
    password = PasswordField(_(u'Password'), validators=[InputRequired()])
