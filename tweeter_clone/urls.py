from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tweets_api.views import UserViewSet, TweetViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tweets', TweetViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
