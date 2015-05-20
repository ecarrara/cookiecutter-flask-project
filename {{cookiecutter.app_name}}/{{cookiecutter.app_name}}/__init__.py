# -*- coding: utf-8 -*-
"""
    {{cookiecutter.project_name}}
    {{'~' * (cookiecutter.project_name|length)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import Flask
from {{cookiecutter.app_name}}.config import DevelopmentConfig


__version__ = '{{cookiecutter.version}}'


def create_app(config=None):
    if config is None:
        config = DevelopmentConfig()

    app = Flask(__name__)

    app.config.from_object(config)
    app.config.from_envvar('{{cookiecutter.app_name|upper}}_CONFIG', silent=True)

    return app
