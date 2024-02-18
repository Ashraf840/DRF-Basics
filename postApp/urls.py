from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homePage, name='homePage'),
    path('list/', views.posts_list, name='posts_list'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
]

