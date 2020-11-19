from datetime import datetime
from django.db import transaction
from rest_framework import serializers
from manager.models import User


# Serializer for creating manager object
class ManagerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, max_length=200,
                                  error_messages={"required": "The field email is required."})
    first_name = serializers.CharField(required=True, max_length=200,
                                       error_messages={"required": "The field firstname is required."})
    last_name = serializers.CharField(required=True, max_length=200,
                                      error_messages={"required": "The field lastname is required."})
    password = serializers.CharField(required=True, max_length=200,
                                     error_messages={"required": "The field password is required."})
    address = serializers.CharField(required=True, max_length=200,
                                    error_messages={"required": "The field address is required."})
    date_of_birth = serializers.CharField(required=True, max_length=200,
                                          error_messages={"required": "The field date of birth is required."})
    company = serializers.CharField(required=True, max_length=200,
                                    error_messages={"required": "The field company is required."})

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            user_obj = super(ManagerSerializer, self).create(validated_data)
            user_obj.set_password(validated_data['password'])
            user_obj.created_date = datetime.utcnow()
            user_obj.updated_date = datetime.utcnow()
            user_obj.is_active = True
            user_obj.is_staff = True
            user_obj.is_manager = True
            user_obj.save()
            return user_obj
