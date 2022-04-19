from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from ..models import Article    # getting 1-directory upward to get the 'models.py' file

from rest_framework.decorators import api_view  # rest_framework decorator
from rest_framework.response import Response    # throw the response in the DRF UI
from ..serializers import ArticleSerializer     # import the serializer
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt  # not required while using the 'POST' api_view


####### Function-based APIs for CRUD operations on "Article"


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'API Overview': 'api/',
        'List': 'api/article-list/',
        'Detail View': 'article/<str:pk>',
        'Create': 'article-create/',
        'Update': 'article-update/<str:pk>/',
        'Delete-specific': 'article-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.order_by('-id')
    # serialize the queryset, along with the param 'many=True', cause there will be multiple data
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponse('No such article is found!', status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def article_update(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def article_delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()

    # after deletion, return the new article-list
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)



