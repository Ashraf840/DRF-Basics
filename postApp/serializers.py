from rest_framework import serializers
from .models import Post


# Plain Serializer
class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=60)
    content=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)

class PostModelSerializer(serializers.ModelSerializer):
    # Add validations for creating or updating posts through this serializer
    title=serializers.CharField(max_length=60)  # Ensures the char limit to 50 while creating/updating any post using this serializer
    # TODO: [Add author inside "Post" table-1] Try to automatically fetch user info from the JWT token & add the user object in the "create()" method of this class. So that, we are not required to add an extra field to each exisiting API to make their create-post request valid.
    class Meta:
        model=Post
        fields=['id','title','content','created_at']