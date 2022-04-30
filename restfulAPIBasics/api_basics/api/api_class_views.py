from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Article
from ..serializers import ArticleSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view


############
# Class-based-api-views:
# Make the code-base DRY. This class-based-API uses two controllers to interact with the end-user/ technology.
#   1. for displaying all article-list & to create new article record.
#   2. for executing retrieve, update & delete operations.
# [Note]: By this approach we can complete the vanilla CRUD operations using two api-endpoints.
############


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'API Overview': 'api/class-based/',
        'List & Create': 'api/class-based/article/',
        'Detail View, Update & Delete': 'api/class-based/article/<str:pk>/',
    }
    return Response(api_urls)


# Handles Article-list, Create API
class ArticleAPIView(APIView):
    # Fetch all articles
    def get(self, request):
        articles = Article.objects.order_by('-id')
        serializer = ArticleSerializer(articles, many=True) # pass the param "many=True", since we're passing a queryset (which may contain multiple articles)
        return Response(serializer.data)

    # Create new article
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Handles Retrieve, Update & Delete API
class ArticleDetail(APIView):
    # a custom func to fetch a particular article from the "Article" table, which will be used in
    # the retrieve,update,delete func
    def get_object(self, id):
        try:
            article = Article.objects.get(id=id)
            return article
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # This class-based api-func is meant to except an extra param as article-id
    def get(self, request, pk):
        article = self.get_object(id=pk)

        # ###### [TESTING]: viewing all the methods & properties of the 'article' object
        # print(article)
        # print(article.status_code)
        # print(article.getvalue())

        # for i in dir(article):
        #     print(i)
        # ###########################

        # Handles if a certain article data isn't found in the DB.

        try:
            if article.status_code == 404:
                return HttpResponse('Article does not exist!', status=status.HTTP_404_NOT_FOUND)    # by sending an HTTPResponse, we're not allowing the client to view the DRF-UI, in order to avoid handling the "put()" & "delete()" functions
                # return Response('Article does not exist!', status=status.HTTP_404_NOT_FOUND)      # [not necessary]: otherwise, we've to customize the "put()", "delete()" functions as well.
        except AttributeError:
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

    # class-based api-func to update an article
    def put(self, request, pk):
        article = self.get_object(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        article = self.get_object(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
