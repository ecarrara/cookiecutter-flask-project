# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.modules.users
    {{'~' * (cookiecutter.app_name|length + 14)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates')
