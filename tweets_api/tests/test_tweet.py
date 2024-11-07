import pytest
from rest_framework import status
from rest_framework.test import APIClient
from tweets_api.models import TweetModel, UserModel

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserModel.objects.create(
        nome="John Doe", senha="password123", profile="https://via.placeholder.com/500x500"
    )


@pytest.fixture
def tweet(user):
    return TweetModel.objects.create(owner=user, post="This is a tweet", image=user.profile)


@pytest.fixture
def api_client():
    return APIClient()


def test_create_tweet(api_client, user):
    url = '/tweets/'
    data = {
        "owner": user.id,
        "post": "This is a new tweet",
        "image": user.profile
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['post'] == "This is a new tweet"


def test_get_tweets(api_client, tweet):
    url = '/tweets/'
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data['results'][0]['post'] == tweet.post


def test_delete_tweet(api_client, tweet):
    url = f'/tweets/{tweet.id}/'
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert TweetModel.objects.count() == 0
