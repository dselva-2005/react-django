from rest_framework.viewsets import ModelViewSet
from rest_framework import filters 

class AbstractViewset(ModelViewSet):
    http_method_names = ('get','put','delete','post')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated','created']
    ordering = ['-updated']