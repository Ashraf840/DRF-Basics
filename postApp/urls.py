from django.urls import path, include
from .views import (
    function_based_views as fbv,
    class_based_views as cbv,
    generic_api_views_and_mixins as gavam,
    views_on_viewsets_and_routers as vovar,
    views_on_model_viewsets as vomv,
)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("", vovar.PostViewset, basename="PostViewset")

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

    # Generic API Views
    path('generic/list-create/', gavam.PostListCreateGenericView.as_view(), name='PostListCreateGenericView'),
    path('generic/retrieve-update-delete/<int:pk>/', gavam.PostRetrieveUpdateDestroyGenericView.as_view(), name='PostRetrieveUpdateDestroyGenericView'),
    # NB: Required to define "pk" as extra param instead of "id" while creating api endpoint using GenericAPIView

    # Viewset API Endpoint
    path('viewset/', include(router.urls)),

    # Model Viewset API Endpoint
    path('model-viewset/', vomv.PostModelViewset.as_view({
        'get': 'list'
        , 'post': 'create'
    }), name='PostModelViewset'),
    path('model-viewset/<int:pk>/', vomv.PostModelViewset.as_view({
        'get': 'retrieve'
        , 'put': 'update'
        , 'delete': 'destroy'
    }), name='PostModelViewset'),
]

