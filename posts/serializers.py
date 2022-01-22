from rest_framework import serializers
from posts.models import Posts,PostsRates

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Posts
        fields = ["id","post_title","post_body"]
        
class PostsRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model= PostsRates
        fields = ["id","likes","dislikes"]