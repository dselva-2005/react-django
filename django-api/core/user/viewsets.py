from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from core.user.serializers import UserSerializer
from core.user.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

class UserViewset(viewsets.ModelViewSet):
    http_method_names = ('patch','get','delete')
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser :
            return User.objects.all()
        
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj
    
    def destroy(self, request, pk=None):
        user = self.get_object()  # raises Http404 if not found, automatically handled by DRF
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
