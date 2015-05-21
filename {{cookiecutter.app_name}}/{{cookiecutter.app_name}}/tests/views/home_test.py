# -*- coding: utf-8 -*-
"""
    {{cookiecutter.app_name}}.tests.views.home_test
    {{'~' * (cookiecutter.project_name|length + 21)}}

    {{cookiecutter.project_description}}

    :author: {{cookiecutter.full_name}} {{cookiecutter.email}}
    :copyright: (c) {{cookiecutter.year}} {{cookiecutter.full_name}}
    :license: {{cookiecutter.license}}, see LICENSE file.
"""

from {{cookiecutter.app_name}}.tests import BaseTestCase


class HomeViewTestCase(BaseTestCase):

    def test_home_response(self):
        response = self.client.get('/')
        self.assert200(response)
