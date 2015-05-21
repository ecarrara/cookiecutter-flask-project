# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.config
    {{'~' * (cookiecutter.project_name|length + 7)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""


class Config(object):

    MODULES = (
        ('users', '/users'),
    )
    ASSETS = '{{cookiecutter.app_name}}/assets.yml'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/{{cookiecutter.app_name}}.db'
    SECRET_KEY = 'changethisinproduction'


class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False


class TestingConfig(Config):

    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
