from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homePage, name='homePage'),
    path('list/', views.posts_list, name='posts_list'),
    path('create/', views.post_create, name='post_create'),
    path('create/model-serializer/', views.post_create_ms, name='post_create_ms'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
    path('detail/db/<int:id>/', views.post_detail_db, name='post_detail_db'),
]

