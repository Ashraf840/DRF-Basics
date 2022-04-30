from rest_framework import generics
from rest_framework import mixins
from ..serializers import ArticleSerializer
from ..models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view

##############
# Generic View API
# Django’s generic views, were developed as a shortcut for common usage patterns.
# These views allow us to build conventional APIs (common views) quickly without repeating ourselves.
# Promoting "DRY principle" by abstracting certain common patterns & idioms in view (API) development with "Generic Views".
##############


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'API Overview': 'api/generic-based/',
        'List & Create': 'api/generic-based/article/',
        'Detail View, Update & Delete': 'api/generic-based/article/<str:id>/',
    }
    return Response(api_urls)


# List, Create API
class ArticleListGenericView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.order_by('-id')

    def get(self, request):
        return self.list(request)

    def post(self, request):
        self.create(request)    # create a new article
        return self.list(request)   # return all the articles record, along with the newly added article


# Retrieve, Update, Destroy API
class ArticleGenericView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id' # assigned as the extra-param in the url-string, using "id" as the value is recommended, cause i've tested using "pk" & it throws an "Unexpected Keyword Argument" error.

    def get(self, request, id):
        return self.retrieve(request, id)   # getting from the "mixins.RetrieveModelMixin"

    def put(self, request, id):
        return self.update(request, id)     # getting from the "mixins.UpdateModelMixin"

    def delete(self, request, id):
        return self.destroy(request, id)    # getting from the "mixins.DestroyModelMixin"
