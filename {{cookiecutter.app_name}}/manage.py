#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.manage
    {{'~' * (cookiecutter.app_name|length + 7)}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}.
    :license: {{cookiecutter.license}}, see LICENSE file.
"""


from flask_script import Manager
from flask_assets import ManageAssets
from flask_migrate import MigrateCommand
from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.config import DevelopmentConfig
from {{cookiecutter.app_name}}.extensions import assets


app = create_app(config=DevelopmentConfig())
manager = Manager(app)

manager.add_command('assets', ManageAssets(assets))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
