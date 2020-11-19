import uuid
import jwt
from common.models.user_token import UserToken
from manager.models import get_manager_by_email, User
from python.constants import SECRET_KEY


# Helper or validating request
def validate_login_data(request):
    if 'email' in request.data and 'password' in request.data:
        return True
    else:
        return False


# Function for login and JWT token generation
def login(request, user):
    try:
        user_obj = get_manager_by_email(user.email)
        payload = {'user_id_string': str(user_obj.id_string), 'string': str(uuid.uuid4().hex[:6].upper())}
        encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        token_obj = UserToken(
            user=user_obj,
            token=encoded_jwt,
            is_active=True
        )
        token_obj.save()
        return token_obj.token
    except Exception as e:
        return False


# Function for checking duplicate user email
def is_email_exists(email):
    return User.objects.filter(email=email, is_active=True).exists()
