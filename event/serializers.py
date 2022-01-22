from rest_framework import serializers

class AddressGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressGlobal
        fields = '__all__'
        
class CustomSerializer(serializers)