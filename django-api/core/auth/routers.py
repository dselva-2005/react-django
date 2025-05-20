from rest_framework import routers
from core.auth.viewsets import RegisterViewset
from core.auth.viewsets import LoginViewset
from core.auth.viewsets import RefreshViewset

auth_router = routers.SimpleRouter(trailing_slash=False)
auth_router.register(r'auth/register',RegisterViewset,basename='auth-register')
auth_router.register(r'auth/login',LoginViewset,basename='auth-login')
auth_router.register(r'auth/refresh',RefreshViewset,basename='auth-refresh')