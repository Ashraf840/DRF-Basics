from django.urls import path, include
from .api import api_views, api_class_views as acv

urlpatterns = [
    # API Endpoints (Function-based-view)
    path('api/', api_views.apiOverview, name='api_overview'),
    path('api/article-list/', api_views.article_list, name='article_list'),
    path('api/article/<str:pk>/', api_views.article_detail, name='article'),
    path('api/article-create/', api_views.article_create, name='article_create'),
    path('api/article-update/<str:pk>/', api_views.article_update, name='article_update'),
    path('api/article-delete/<str:pk>/', api_views.article_delete, name='article_delete'),

    # API Endpoints (Class-based-view)
    path('api/class-based/', acv.apiOverview, name='api_overview'),
    path('api/class-based/article-list/', acv.ArticleAPIView.as_view(), name='articleList_classBased'),   # since it's a class-based API, require to mention ".as_views()" explicitly.
    path('api/class-based/article-detail/<str:pk>/', acv.ArticleDetail.as_view(), name='article_classBased'), # this "pk" param is used inside the "get()" func of the class "ArticleDetail"
]