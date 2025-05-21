from core.user.routers import user_router
from core.auth.routers import auth_router
from core.post.routers import post_router

urlpatterns = [
    *user_router.urls,
    *auth_router.urls,
    *post_router.urls,
]
