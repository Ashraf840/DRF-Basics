# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

# # API without using django-rest-framework
# def homePage(request:HttpResponse):
#     response={"message":"Hello World"}
#     return JsonResponse(data=response)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PostSerializer as PlainPostSerializer
from .models import Post


# Mock a simple database table by enlisting 3 posts
posts = [
    {
        "id":1,
        "title":"Why is it difficult to learn programming?",
        "content":"This is to give reasons why it is hard"
    },
    {
        "id":2,
        "title":"Learn JavaScript",
        "content":"This a course on JS"
    },
    {
        "id":3,
        "title":"Why is it difficult to learn programming?",
        "content":"This is to give reasons why it is hard"
    },
]

# Function-based api-view
@api_view(http_method_names=["GET", "POST"])
def homePage(request:Request):
    if request.method == "POST":
        data=request.data
        response={
            "message":"Hello World",
            "data":data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    response={"message":"Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def posts_list(request:Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request, id:int):
    post=posts[id]
    if posts:
        return Response(data=post, status=status.HTTP_200_OK)
    return Response(data={"error":"Not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=["POST"])
def post_create(request:Request):
    if request.method == "POST":
        new_post=Post(
            title=request.data.get("title"),
            content=request.data.get("content"),
        )
        new_post.save()
        # Just serializing the data to send as a json response
        serializer=PlainPostSerializer(instance=new_post)
        print(serializer)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)