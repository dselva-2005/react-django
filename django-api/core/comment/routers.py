from rest_framework_nested import routers
from core.comment.viewsets import CommentViewset

comment_route = routers.SimpleRouter(trailing_slash=False)
comment_route.register(r'comment',CommentViewset,basename='comment')