from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from manager.serializers.manager import ManagerSerializer
from manager.views.helper import *
from python.constants import *


# API Header
# API end Point: api/v1/user/login
# API verb: POST
# Usage: Add
# Tables used: User
# Author: Rohan
# Created on: 18/11/2020
class LoginApiView(GenericAPIView):
    def post(self, request):
        try:
            if validate_login_data(request):
                email = request.data['email']
                password = request.data['password']
                auth = authenticate(email=email, password=password)
                if auth is not None:
                    token = login(request, auth)
                    return Response({
                        STATE: SUCCESS,
                        TOKEN: token,
                        MESSAGE: LOGIN_SUCCESSFULLY
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        STATE: FAILED,
                        MESSAGE: INVALID_CREDENTIAL
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    STATE: FAILED,
                    MESSAGE: LOGIN_FAILED
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                STATE: EXCEPTION,
                MESSAGE: EXCEPTION
            }, status=status.HTTP_400_BAD_REQUEST)


# API Header
# API end Point: api/v1/user/login
# API verb: POST
# Usage: Add
# Tables used: User
# Author: Rohan
# Created on: 18/11/2020
class ManagerApiView(GenericAPIView):
    def post(self, request):
        try:
            serializer = ManagerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                if not is_email_exists(request.data['email']):
                    user_obj = serializer.create(serializer.validated_data)
                    return Response({
                        STATE: SUCCESS,
                        MESSAGE: CREATED_SUCCESSFULLY
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        STATE: FAILED,
                        MESSAGE: ALREADY_EXISTS
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    STATE: FAILED,
                    MESSAGE: list(serializer.errors.values())[0][0],
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                STATE: EXCEPTION,
                MESSAGE: EXCEPTION
            }, status=status.HTTP_400_BAD_REQUEST)
