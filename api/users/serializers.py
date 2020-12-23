from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'profilepic', 'last_login', 'member_since', 'first_name', 'last_name', 'email', 'slug', 'phone_number', 'about_you')
