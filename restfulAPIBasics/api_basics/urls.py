from django.urls import path, include
from .api import api_overview as api_o, api_func_views as afv, api_class_views as acv

urlpatterns = [
    # API Endpoints Overview
    path('api/', api_o.apiOverview, name='api_overview'),

    # API Endpoints (Function-based-view)
    path('api/func-based/', afv.apiOverview, name='api_overview_func'),
    path('api/func-based/article-list/', afv.article_list, name='api_func_article_list'),
    path('api/func-based/article/<str:pk>/', afv.article_detail, name='api_func_article'),
    path('api/func-based/article-create/', afv.article_create, name='api_func_article_create'),
    path('api/func-based/article-update/<str:pk>/', afv.article_update, name='api_func_article_update'),
    path('api/func-based/article-delete/<str:pk>/', afv.article_delete, name='api_func_article_delete'),

    # API Endpoints (Class-based-view)
    path('api/class-based/', acv.apiOverview, name='api_overview_class'),
    path('api/class-based/article-list/', acv.ArticleAPIView.as_view(), name='api_class_articleList'),   # since it's a class-based API, require to mention ".as_views()" explicitly.
    path('api/class-based/article-detail/<str:pk>/', acv.ArticleDetail.as_view(), name='api_class_article'), # this "pk" param is used inside the "get()" func of the class "ArticleDetail"
]
