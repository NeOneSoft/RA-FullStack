from rest_framework.test import RequestsClient

from django.test import TestCase


class BookUrlTest(TestCase):
    def test_books_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/books/')

        self.assertEqual(response.status_code, 200)

    def test_books_detail(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/books/1/')

        self.assertEqual(response.status_code, 404)

