from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.serializers import CustomSerializer,CustomUser, UserProfile, UserProfileSerializer



class CustomUserView(ModelViewSet):
    serializer_class = CustomSerializer
    queryset = CustomUser.objects.all()
    
class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    
