from rest_framework import viewsets
from ..models import Post
from ..serializers import PostModelSerializer


class PostModelViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostModelSerializer
