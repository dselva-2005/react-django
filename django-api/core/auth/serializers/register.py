from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    """registration serializer for requests and user creation"""
    # make sure the password is 8 characters long and not longer than 128 and cant read by user 
    password = serializers.CharField(max_length=128,write_only=True,required=True,min_length=8)

    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email','username', 'first_name', 'last_name','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)