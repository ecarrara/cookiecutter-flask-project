# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.deploy
    {{'~' * (cookiecutter.project_name|length + 7)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.config import ProductionConfig

app = create_app(config=ProductionConfig())
