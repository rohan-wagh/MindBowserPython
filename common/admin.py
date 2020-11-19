from django.contrib import admin
from common.models.user_token import UserToken

# Register tables in django admin
admin.site.register(UserToken)
