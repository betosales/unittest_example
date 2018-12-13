import unittest
from app import app


class BaseConfig(unittest.TestCase):
    """
    Essa classe irá ser a base para os outros testes.
    """

    def setUp(self):
        self.app = app.test_client()
