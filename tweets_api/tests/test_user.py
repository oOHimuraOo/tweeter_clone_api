import pytest
from rest_framework import status
from rest_framework.test import APIClient
from tweets_api.models import UserModel

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserModel.objects.create(
        nome="John Doe", senha="password123", profile="https://via.placeholder.com/500x500"
    )


@pytest.fixture
def api_client():
    return APIClient()


def test_create_user(api_client):
    url = '/users/'
    data = {
        "nome": "Jane Doe",
        "senha": "password456",
        "profile": "https://via.placeholder.com/500x500",
        "logged_in": False
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['nome'] == "Jane Doe"


def test_get_users(api_client, user):
    url = '/users/'
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data['results'][0]['nome'] == user.nome


def test_delete_user(api_client, user):
    url = f'/users/{user.id}/'
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert UserModel.objects.count() == 0
