# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.extensions
    {{'~' * (cookiecutter.project_name|length + 11)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


assets = Environment()
db = SQLAlchemy()
migrate = Migrate()
