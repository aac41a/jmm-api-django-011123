# api_py/utils.py

from rest_framework_simplejwt.tokens import RefreshToken

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'email': user.email,
    }