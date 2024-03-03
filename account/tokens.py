from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User=get_user_model()

def create_jwt_pair(user:User): # type: ignore
    refresh=RefreshToken.for_user(user) # It's adding this token to outstanding token list which is a hidden table (OutstandingToken). This will be visible 
    tokens={
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }
    return tokens
