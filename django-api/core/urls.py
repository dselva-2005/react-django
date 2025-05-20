from core.user.routers import user_router
from core.auth.routers import auth_router

urlpatterns = [
    *user_router.urls,
    *auth_router.urls,
]
