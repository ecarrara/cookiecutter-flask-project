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
    pass


class DevelopmentConfig(Config):

    DEBUG = True
