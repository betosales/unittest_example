import unittest

from app import app
from tests.test_config import BaseConfig


class TestIndex(BaseConfig):
    """
    Essa classe irá testar tudo referente ao index.
    """

    def test_status_code_in_index_is_200(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
