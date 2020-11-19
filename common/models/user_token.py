import uuid
from datetime import datetime
from django.db import models
from manager.models import User


# Actual user token table start
class UserToken(models.Model):
    id_string = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    token = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_by = models.BigIntegerField(null=True, blank=True)
    updated_by = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, default=datetime.now())
    updated_date = models.DateTimeField(null=True, blank=True, default=datetime.now())

    def __str__(self):
        return self.token

    def __unicode__(self):
        return self.token
