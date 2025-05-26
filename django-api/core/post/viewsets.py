from abstract.viewsets import AbstractViewset
from core.post.serializers import PostSerializer
from rest_framework.response import Response
from core.post.models import Post
from rest_framework import status
from core.auth.permissions import UserPermission
from rest_framework.decorators import action

class PostViewset(AbstractViewset):
    http_method_names = ('get','post','delete','put')
    serializer_class = PostSerializer
    permission_classes = (UserPermission,)

    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        obj = Post.objects.get(public_id=self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj
    
    def create(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    @action(methods=['post'],detail=True)
    def like(self,request,*args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.like(post)
        serializer = self.serializer_class(post)
        Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=True)
    def remove_like(self,request,*args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)
        Response(serializer.data,status=status.HTTP_200_OK)