from abstract.serializers import AbstractSerializer
from core.post.models import Post
from rest_framework import serializers
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer
from rest_framework.exceptions import ValidationError

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_liked(self,instance):
        request = self.context.get('request',None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)

    def get_likes_count(self,instance):
        return instance.liked_by_user.count()

    def validate_author(self,value):
        if self.context['request'].user != value:
            raise ValidationError('You cannot create post for other user')
        

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(rep)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        
        return super().update(instance, validated_data)

    class Meta:
        model = Post
        fields = ['id','author','edited','created','updated','body','liked','likes_count']
        read_only_fields = ['edited']