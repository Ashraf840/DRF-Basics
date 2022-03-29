from django.urls import path, include
from .api import api_views

urlpatterns = [
    # API Endpoints
    path('api/', api_views.apiOverview, name='api-overview'),
    path('api/article-list/', api_views.article_list, name='article-list'),
    path('api/article/<str:pk>', api_views.article_detail, name='article'),
    path('api/article-create/', api_views.article_create, name='article_create'),
    path('api/article-update/<str:pk>/', api_views.article_update, name='article_update'),
    path('api/article-delete/<str:pk>/', api_views.article_delete, name='article_delete'),
]