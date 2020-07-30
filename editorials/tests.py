from rest_framework.test import RequestsClient

from django.test import TestCase


class EditorialUrlTest(TestCase):

    def test_editorials_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/editorials/')

        self.assertEqual(response.status_code, 200)

    def test_editorials_detail(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/editorials/1/')

        self.assertEqual(response.status_code, 404)
