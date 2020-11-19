import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Actual user table start
class User(AbstractBaseUser, PermissionsMixin, BaseUserManager):
    id_string = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = None
    password = models.CharField(max_length=200, verbose_name='password')
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True, default=datetime.now())
    email = models.CharField(max_length=200, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects = MyUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email


def get_manager_by_email(email):
    return User.objects.get(email=email, is_active=True)


def get_all_employee():
    return User.objects.filter(is_employee=True, is_active=True)
