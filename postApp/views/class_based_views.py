from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from ..serializers import PostModelSerializer
from ..models import Post
from django.shortcuts import get_object_or_404

"""
Notes (APIView): Unlike function-based views, the methods can be defined together under classes. 
Like listing-out all the data & creating a record using same api endpoint. 
Similarly, the get-record-by-id, update-specific-record, delete-specific-record, 
all these three functionalities can be achieved using a single endpoint.
No need to define scrattered functions to obtain those functionalities.
Moreover, it take less urls-paths to be defined in the urlpatterns.
"""

class PostListCreateView(APIView):

    serializer_class=PostModelSerializer

    def get(self, request:Request):
        posts=Post.objects.all()
        serializer=self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)   # TODO: [Add author inside "Post" table-2] automatically get user-info from the JWT token passed with the "header" of a request before adding that user as author;
            response={
                "message":"Post created",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(APIView):

    serializer_class=PostModelSerializer

    def get(self, request:Request, id:int):
        post=get_object_or_404(Post, pk=id)
        serializer=self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request:Request, id:int):
        post=get_object_or_404(Post, pk=id)
        data=request.data
        serializer=self.serializer_class(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id:int):
        post=get_object_or_404(Post, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)