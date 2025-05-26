from django.db import models
from abstract.models import AbrstractManager,AbrstractModel

class CommentManager(AbrstractManager):
    pass

class Comment(AbrstractModel):
    post = models.ForeignKey("core_post.Post",on_delete=models.PROTECT)
    author = models.ForeignKey("core_user.User",on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = CommentManager()

    def __str__(self):
        return self.author.name