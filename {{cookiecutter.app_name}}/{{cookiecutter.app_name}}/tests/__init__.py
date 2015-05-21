# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.tests
    {{'~' * (cookiecutter.project_name|length + 6)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from flask_testing import TestCase
from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.config import TestingConfig
from {{cookiecutter.app_name}}.extensions import assets


class BaseTestCase(TestCase):

    def create_app(self):
        assets._named_bundles = {}
        app = create_app(config=TestingConfig())
        return app
