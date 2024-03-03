from django.db import models
from django.contrib.auth import get_user_model


user=get_user_model()


class Post(models.Model):
    title=models.CharField(max_length=60)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(user, on_delete=models.CASCADE, related_name="posts")  # "related_name" will create the reverse relationship from the "user" to "posts" table

    def __str__(self) -> str:
        return self.title
