from django.urls import path
from .views import UserSignupGenericView


urlpatterns = [
    path('user/signup/', UserSignupGenericView.as_view(), name='UserSignupGenericView'),
]

