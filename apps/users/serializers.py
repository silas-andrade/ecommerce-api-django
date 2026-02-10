from rest_framework import serializers

from .models import User, Customer

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'full_name', 
            'created_at'
            ] 
        

class ReadCustomerSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = [
            'id',
            'user',
            'profile_image',
            'address'
        ]