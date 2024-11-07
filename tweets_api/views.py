from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel, TweetModel
from .serializers import UserSerializer, TweetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all().order_by('id')
    serializer_class = UserSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = TweetModel.objects.all().order_by('id')
    serializer_class = TweetSerializer

