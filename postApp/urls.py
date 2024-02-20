from django.urls import path
from .views import (
    function_based_views as fbv,
    class_based_views as cbv,
)

urlpatterns = [
    # Function Based Views
    path('homepage/', fbv.homePage, name='homePage'),
    path('list/', fbv.posts_list, name='posts_list'),
    path('create/', fbv.post_create, name='post_create'),
    path('create/model-serializer/', fbv.post_create_ms, name='post_create_ms'),
    # path('detail/<int:id>/', fbv.post_detail, name='post_detail'),
    path('detail/db/<int:id>/', fbv.post_detail_db, name='post_detail_db'),
    path('update/<int:id>/', fbv.post_update, name='post_update'),
    path('delete/<int:id>/', fbv.post_delete, name='post_delete'),

    # Class Based Views
    path('class/list-create/', cbv.PostListCreateView.as_view(), name='PostListCreateView'),
    path('class/retrieve-update-delete/<int:id>/', cbv.PostRetrieveUpdateDeleteView.as_view(), name='PostRetrieveUpdateDeleteView'),
]

