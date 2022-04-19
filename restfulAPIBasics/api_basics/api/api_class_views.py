from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Article
from ..serializers import ArticleSerializer
from django.http import HttpResponse


############
# Class-based-api-views:
# Make the code-base DRY. This class-based-API uses a single controller to interact with the end-user/ technology.
############

class ArticleAPIView(APIView):
    # fetch all articles
    def get(self, request):
        articles = Article.objects.order_by('-id')
        serializer = ArticleSerializer(articles, many=True) # pass the param "many=True", since we're passing a queryset (which may contain multiple articles)
        return Response(serializer.data)

    # # fetch a particular article
    # def retrieve(self, request, pk):
    #     try:
    #         article = Article.objects.get(id=pk)
    #     except Article.DoesNotExist:
    #         return HttpResponse('No such article is found!', status=status.HTTP_404_NOT_FOUND)
    #     serializer = ArticleSerializer(article, many=False)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


