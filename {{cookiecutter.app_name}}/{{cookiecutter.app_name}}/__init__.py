# -*- coding: utf-8 -*-
"""
    {{cookiecutter.project_name}}
    {{'~' * (cookiecutter.project_name|length)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask import Flask, render_template
from {{cookiecutter.app_name}}.config import DevelopmentConfig
from {{cookiecutter.app_name}}.extensions import assets, db, migrate


__version__ = '{{cookiecutter.version}}'


def create_app(config=None):
    if config is None:
        config = DevelopmentConfig()

    app = Flask(__name__)

    app.config.from_object(config)
    app.config.from_envvar('{{cookiecutter.app_name|upper}}_CONFIG', silent=True)

    assets.init_app(app)
    assets.from_yaml(app.config['ASSETS'])

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app
