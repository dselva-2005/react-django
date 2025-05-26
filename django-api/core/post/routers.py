from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import SimpleRouter
from core.post.viewsets import PostViewset
from core.comment.viewsets import CommentViewset


post_router = SimpleRouter(trailing_slash=False)
post_router.register(r'post',PostViewset,basename='post')
nest_post_router = NestedSimpleRouter(post_router,r'post',lookup='post')
nest_post_router.register(r'comment',CommentViewset,basename='post-comment')