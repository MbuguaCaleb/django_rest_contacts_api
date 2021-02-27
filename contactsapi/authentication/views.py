from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
# Create your views here.


class RegisterView(GenericAPIView):

    serlializer_class = UserSerializer

    def post(self, request):
        # passing data to our serializer
        serializer = UserSerializer(data=request.data)

        # running validate method from the serializer
        # runs validate method
        if serializer.is_valid():
            # runs create method
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # throwing error if the above fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInView(GenericAPIView):
    def post(self, request):
        # getting data from the request
        data = request.data

        # retriving data from the dictionary
        username = data.get('username', '')
        password = data.get('password', '')

        # verifies if the password and username do march
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY,)

            # i also return the response through the serializer meta data
            # This returns me a user object from the userserializer
            serializer = UserSerializer(user)

            data = {
                'user': serializer.data,
                'token': auth_token
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
