from rest_framework.test import RequestsClient


def test_server_request():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000')

    assert response.status_code == 404


def test_url_mutation():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/api/v1/POST/mutation')

    assert response.status_code == 403


def test_url_docs():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/docs')

    assert response.status_code == 403
