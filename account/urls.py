from django.urls import path
from .views import UserSignupGenericView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # create/obtain new access token
    TokenRefreshView, # get new access token using valid refresh token
    TokenVerifyView, # verify the validity of access token
)


urlpatterns = [
    path('user/signup/', UserSignupGenericView.as_view(), name='UserSignupGenericView'),
    path('user/login/', LoginAPIView.as_view(), name='LoginAPIView'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='TokenRefreshView'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='TokenVerifyView'),
]

