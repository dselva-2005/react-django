from rest_framework.routers import SimpleRouter
from core.post.viewsets import PostViewset

post_router = SimpleRouter(trailing_slash=False)
post_router.register(r'post',PostViewset,basename='post')