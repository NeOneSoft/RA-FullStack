from django.urls import reverse
from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from django.test import TestCase, Client

from .forms import AuthorForm
from .models import Author


# Model Author test
class AuthorModelTest(TestCase):

    def create_author(self, first_name="Name_test", last_name="Last_test", birth_date="1980-06-10", phone="78546374"):
        return Author.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date, phone=phone)

    def test_author_creation(self):
        a = self.create_author()
        self.assertTrue(isinstance(a, Author))
        self.assertEqual(a.__str__(), a.first_name)


# API Author test
class AuthorApiTest(APITestCase):

    def test_authors_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/authors/')

        self.assertEqual(response.status_code, 200)

    def test_authors_detail(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/authors/1/')

        self.assertEqual(response.status_code, 404)

    def test_authors_create(self):
        client = RequestsClient()
        data = {'first_name': 'Tom',
                'last_name': 'Hoggans',
                'birth_date': '1950-12-09',
                'phone': '78659874'
                }
        response = client.post('http://127.0.0.1:8000/api/v1/authors/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Forms Author test
class AuthorFormsTest(TestCase):
    def test_valid_form(self):
        a = Author.objects.create(first_name="Name_test", last_name="Last_test", birth_date="1980-06-10",
                                  phone="78546374")
        data = {'first_name': a.first_name, 'last_name': a.last_name, 'birth_date': a.birth_date, 'phone': a.phone}
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Author.objects.create(first_name="Name_test", last_name="", birth_date="1980-06-10", phone="78546374")
        data = {'first_name': a.first_name, 'last_name': a.last_name, 'birth_date': a.birth_date, 'phone': a.phone}
        form = AuthorForm(data=data)
        self.assertFalse(form.is_valid())


class AuthorListViewTest(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get('http://127.0.0.1:8000/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/authors_list.html')
