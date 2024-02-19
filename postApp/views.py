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
from .serializers import PostSerializer as PlainPostSerializer, PostModelSerializer
from .models import Post
from django.shortcuts import get_object_or_404


# Mock a simple database table by enlisting 3 posts
# posts = [
#     {
#         "id":1,
#         "title":"Why is it difficult to learn programming?",
#         "content":"This is to give reasons why it is hard"
#     },
#     {
#         "id":2,
#         "title":"Learn JavaScript",
#         "content":"This a course on JS"
#     },
#     {
#         "id":3,
#         "title":"Why is it difficult to learn programming?",
#         "content":"This is to give reasons why it is hard"
#     },
# ]

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
    # Get the posts from db & jsonify them using the model serializer
    posts = Post.objects.all()
    serializer=PostModelSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# Using native python list to mock fetch post record from db
@api_view(http_method_names=["GET"])
def post_detail(request:Request, id:int):
    post=posts[id]
    if posts:
        return Response(data=post, status=status.HTTP_200_OK)
    return Response(data={"error":"Not found"}, status=status.HTTP_404_NOT_FOUND)

# Used plain serializer: PostSerializer
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
        response={
            "message":"Post created",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)

# Used model serializer: PostModelSerializer
@api_view(http_method_names=["POST"])
def post_create_ms(request:Request):
    if request.method == "POST":
        data={
            "title":request.data.get('title'),
            "content":request.data.get('content'),
        }
        serializer=PostModelSerializer(data=data)   # while creating, use "data" kwargs
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"Post created",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
def post_detail_db(request:Request, id:int):
    post=get_object_or_404(Post,pk=id)
    print("post:", post)
    # Serailize the post object fetched from db, then jasonify that
    serializer=PostModelSerializer(instance=post)   # while fetching, use "instance" kwargs
    # NB: Since I'm serializing an existing post instance, there's no need to call the ".is_valid()" method of the serializer.
    response={
        "message":"Post found",
        "data":serializer.data
    }
    # Must Required to invoke the ".is_valid()" method before accessing the ".data" of the serializer
    return Response(data=response, status=status.HTTP_200_OK)

    """
    The issue of using "data" instead of "instance' as the 
    param of "PostModelSerializer": When I'm using "data" param, it's 
    required to invoke the ".is_valid()" method before accessing the 
    ".data" from the serializer. On the other hand, the if we use 
    "instance" as param, still invoking the ".is_valid()" method, then
    the serializer will throw an error for not passing any data to 
    the serializer.
    Thus, while processing existing record instance through a serializer,
    use the "instance" param. And use the "data" param while passing data
    from outside to the serializer to make any manipulation to the
    associated db table.
    """