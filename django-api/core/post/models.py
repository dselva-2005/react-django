from abstract.models import AbrstractManager,AbrstractModel
from django.db import models

class PostManager(AbrstractManager):
    def create_post(self):
        pass

class Post(AbrstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE,related_name='posts')
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.author.name
    
    class Meta:
        db_table = "'core.post'"
