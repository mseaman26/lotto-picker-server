from rest_framework import serializers
from .models import LottoPick
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class UserSerializer(serializers.ModelSerializer):

    # prevent password from being returned in response
    password = serializers.CharField(write_only=True, required=True, validators=[MinLengthValidator(8)])

    email = serializers.EmailField(
        required=True,
        error_messages={'invalid': 'Enter a valid email address.'}  # Custom error message for invalid email
    )
    class Meta:
        model = User
        fields = ( 'username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class LottoPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = LottoPick
        fields = '__all__'

