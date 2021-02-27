import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response


class JWTAuthentication(authentication.BaseAuthentication):
    # we override a method called authenticate
    # This is where we as well write all our authentication logic
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        # Token comes as a key value pair<bearer:token>
        # below code  decodes it .Utf-8 converts the data into a string
        prefix, token = auth_data.decode('utf-8').split(' ')
      # print(token)

        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            print(payload)

            user = User.objects.get(username=payload['username'])

            return(user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')

        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')

        return super().authenticate(request)
