from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    # defines what  a user is going to see in the response
    # this is the data that is returned by our API
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    # Validate Method is called before any other method
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                'email', ('Email  is already in use')
            })
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)
