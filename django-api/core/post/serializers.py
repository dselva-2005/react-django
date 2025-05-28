from abstract.serializers import AbstractSerializer
from core.post.models import Post
from rest_framework import serializers
from core.user.models import User
from core.user.serializers import UserSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_liked(self, instance):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)

    def get_likes_count(self, instance):
        return instance.liked_by_user.count()

    def validate_author(self, value):
        request = self.context.get('request')
        if request is None or request.data["author"] != value.public_id.hex:
            raise ValidationError('You cannot create a post for another user.')
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Remove print(rep) in production
        author = get_object_or_404(User, public_id=rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        return super().update(instance, validated_data)

    class Meta:
        model = Post
        fields = ['id', 'author', 'edited', 'created', 'updated', 'body', 'liked', 'likes_count']
        read_only_fields = ['edited']
