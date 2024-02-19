from rest_framework import serializers
from .models import Post


# Plain Serializer
class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=60)
    content=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','content','created_at']