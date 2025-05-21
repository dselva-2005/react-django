from abstract.serializers import AbstractSerializer
from core.post.models import Post
from rest_framework import serializers
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer
from rest_framework.exceptions import ValidationError

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='public_id')

    def validate_author(self,value):
        if self.context['request'].user != value:
            raise ValidationError('You cannot create post for other user')
        

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(rep)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep

    class Meta:
        model = Post
        fields = ['id','author','edited','created','updated','body']
        read_only_fields = ['edited']