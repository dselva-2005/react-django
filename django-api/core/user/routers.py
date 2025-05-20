from rest_framework import routers
from core.user.viewsets import UserViewset

user_router = routers.SimpleRouter(trailing_slash=False)
user_router.register(r'user',UserViewset,basename='user')
