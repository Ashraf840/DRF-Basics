from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from ..serializers import PostModelSerializer
from ..models import Post
from django.shortcuts import get_object_or_404


"""
Notes (GenericAPIView)
Notes (mixins.XModelMixins)
"""

class PostListCreateGenericView(
    generics.GenericAPIView
    , mixins.ListModelMixin
    , mixins.CreateModelMixin
):
    serializer_class=PostModelSerializer
    queryset=Post.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # Probably, the "self.list()" method is only invoking the queryset attribute of this class
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

