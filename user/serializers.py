from dataclasses import fields
from rest_framework import serializers
from .models import CustomUser, UserProfile, AddressGlobal

class AddressGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressGlobal
        fields = '__all__'

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email","name","created_at","updated_at")
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomSerializer()
    address_info = AddressGlobalSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'