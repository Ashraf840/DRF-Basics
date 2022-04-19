from rest_framework import serializers
from .models import Article


# # Serializer class for 'Article'
# class ArticleSerializers(serializers.Serializer):
#     # same fields from the model 'Article'
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateField(auto_now_add=True)
#
#     # create func
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     # update func
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         # lastly, save() the instance
#         return instance


# Model Serializer class for model 'Article'
# It's more like the django's form; used to serialize the data into native python dict.
# Make the code a bit more concise, since ModelSerializer dedicatedly deals with model instances & querysets.
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'date']
        # fields = '__all__'


