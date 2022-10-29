# Django Imports
from django.shortcuts import render

# Rest Framework Imports
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request

# Own Imports
from tweep.models import Tweet
from tweep.serializers import TweetSerializer


def tweep_home(request):
    return render(request, "tweep/tweets.html")


class GetCreateTweetAPIView(generics.GenericAPIView):
    """Responsible for retrieving all tweets and also creating new ones."""
    
    serializer_class = TweetSerializer
    
    def get(self, request:Request) -> Response:
        """Responsible for retrieving all the tweets in the database."""
        
        tweets = Tweet.objects.all()
        serializer = self.serializer_class(tweets, many=True)
        
        payload = {
            "status": status.HTTP_200_OK,
            "message": "Tweets retrieved!",
            "data": serializer.data
        }
        return Response(data=payload, status=status.HTTP_200_OK)
    
    def post(self, request:Request) -> Response:
        """Responsible for creating a new tweet."""
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        payload = {
            "status": status.HTTP_201_CREATED,
            "message": "Birdie flyy!",
            "data": serializer.data
        }
        return Response(data=payload, status=status.HTTP_201_CREATED)