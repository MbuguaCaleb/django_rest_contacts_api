from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
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
            return Response(serializer.data, status.HTTP_201_CREATE)

        # throwing error if the above fails
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
