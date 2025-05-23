from rest_framework.viewsets import ModelViewSet
from rest_framework import filters 

class AbstractViewset(ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated','created']
    ordering = ['-updated']