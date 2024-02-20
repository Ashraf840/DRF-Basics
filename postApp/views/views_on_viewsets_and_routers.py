from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets
from ..serializers import PostModelSerializer
from ..models import Post
from django.shortcuts import get_object_or_404


"""
Notes (Viewsets)
Notes (Routers)
"""

class PostViewset(viewsets.ViewSet):

    def list(self, request:Request):
        queryset=Post.objects.all()
        serializer=PostModelSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk:int): # "pk" as param is required instead of "id" or any other names, since the router instance passes "pk" as extra kwargs into this viewset's retrieve method
        queryset=get_object_or_404(Post, pk=pk)
        serializer=PostModelSerializer(instance=queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request:Request):
        data=request.data
        serializer=PostModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request:Request, pk:int):
        queryset=get_object_or_404(Post, pk=pk)
        data=request.data
        serializer=PostModelSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, pk:int):
        queryset=get_object_or_404(Post, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

