from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    """
    This is the login serializer used for authentication
    """
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})


class CustomRegisterSerializer(RegisterSerializer):
    """
    This is the registration serializer used for authentication
    """
    username = None
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
