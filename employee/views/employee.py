from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from common.views.custom_exception import CustomAPIException
from common.views.pagination import StandardResultsSetPagination
from employee.serializers.employee import EmployeeSerializer, EmployeeListSerializer
from manager.models import get_all_employee
from manager.views.helper import is_email_exists
from python.constants import *


# API Header
# API end Point: api/v1/employee
# API verb: POST
# Usage: Add
# Tables used: User
# Author: Rohan Wagh
# Created on: 18/11/2020
class EmployeeApiView(GenericAPIView):
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
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


# API Header
# API end Point: api/v1/employee/list
# API verb: GET
# Usage: Get
# Tables used: User
# Author: Rohan Wagh
# Created on: 18/11/2020
class EmployeeList(generics.ListAPIView):
    try:
        serializer_class = EmployeeListSerializer
        pagination_class = StandardResultsSetPagination
        filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
        filter_fields = ('first_name',)
        ordering_fields = ('first_name',)
        ordering = ('date_of_birth',)
        search_fields = ('first_name', 'last_name',)

        def get_queryset(self):
            return get_all_employee()

    except Exception as e:
        raise CustomAPIException("Exceptions in getting employee list", status_code=status.HTTP_404_NOT_FOUND)
