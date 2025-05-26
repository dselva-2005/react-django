
from django.http import Http404
from core.comment.serializers import CommentSerializer
from abstract.viewsets import AbstractViewset
from rest_framework.permissions import IsAuthenticated
from core.comment.models import Comment
from rest_framework.response import Response
from rest_framework import status

class CommentViewset(AbstractViewset):
    serializer_class = CommentSerializer
    http_method_names = ('post','get','delete','put')
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            raise Http404

        queryset = Comment.objects.filter(post__public_id=post_pk)

        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)