# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.tasks
    {{'~' * (cookiecutter.project_name|length + 5)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from os import environ
from celery import Celery
from {{cookiecutter.app_name}} import config
from {{cookiecutter.app_name}}.extensions import assets


celery = Celery(__name__)

env = environ.get('{{cookiecutter.app_name|upper}}_ENVIRONMENT', 'DEVELOPMENT')
cfg = getattr(config, '{0}Config'.format(env.capitalize()))

celery.conf.add_defaults(cfg)


class ContextTask(celery.Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        from {{cookiecutter.app_name}} import create_app

        assets._named_bundles = {}
        with create_app(cfg).app_context():
            return super(ContextTask, self).__call__(*args, **kwargs)

celery.Task = ContextTask
