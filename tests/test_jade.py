import unittest

from app import app
from tests.test_config import BaseConfig


class TestJade(BaseConfig):
    """
    Essa classe irá testar tudo referente ao index.
    """

    def test_jade_endpoint_has_jaderesca(self):
        resp = self.app.get('/jade')
        self.assertIn('jaderesca', resp.data.decode('utf-8'))

    def test_jade_endpoint_status_code_is_200(self):
        resp = self.app.get('/jade')
        self.assertEqual(resp.status_code, 200)
