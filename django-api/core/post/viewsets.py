from abstract.viewsets import AbstractViewset
from core.post.serializers import PostSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from core.post.models import Post
from rest_framework import status

class PostViewset(AbstractViewset):
    http_method_names = ('get','post')
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

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
    