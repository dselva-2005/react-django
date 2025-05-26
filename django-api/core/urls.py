from core.user.routers import user_router
from core.auth.routers import auth_router
from core.post.routers import post_router,nest_post_router
from core.comment.routers import comment_route

urlpatterns = [
    *user_router.urls,
    *auth_router.urls,
    *post_router.urls,
    *comment_route.urls,
    *nest_post_router.urls,
]
