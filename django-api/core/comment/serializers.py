from abstract.serializers import AbstractSerializer
from rest_framework import serializers
from core.comment.models import Comment
from core.user.models import User
from core.post.models import Post
from core.post.serializers import PostSerializer
from core.user.serializers import UserSerializer

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id'
    )
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='public_id'
    )

    def validate_post(self,value):
        if self.instance:
            return self.instance.post
        return value
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
            
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(user).data
        post = Post.objects.get_object_by_public_id(rep['post'])
        rep['post'] = PostSerializer(post).data
        return rep

    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj 
    
    class Meta:
        model = Comment
        fields = ['post', 'author', 'edited', 'created', 'updated']
        read_only_fields = ['created', 'updated']
