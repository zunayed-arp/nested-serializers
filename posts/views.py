from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from posts.models import Posts, PostsRates
from posts.serializers import PostSerializer, PostsRatesSerializer

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        posts = Posts.objects.all()
        return Posts
    
class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer
    
    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates
    
