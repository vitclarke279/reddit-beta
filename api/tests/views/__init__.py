from unittest import TestCase

from fastapi.testclient import TestClient

from start_api import app


class ApiTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = TestClient(app)
