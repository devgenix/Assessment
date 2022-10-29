# Django Imports
from django.urls import path

# Own Imports
from tweep.views import GetCreateTweetAPIView


urlpatterns = [
    path("tweet/", GetCreateTweetAPIView.as_view(), name="get_create_tweet"),
]
