from rest_framework import serializers
from .models import UserModel, TweetModel


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'nome', 'senha', 'profile', 'logged_in', 'tweets']


class TweetSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.nome', read_only=True)
    image = serializers.CharField(source='owner.profile', read_only=True)

    class Meta:
        model = TweetModel
        fields = ['id', 'owner', 'owner_name', 'image', 'post']
