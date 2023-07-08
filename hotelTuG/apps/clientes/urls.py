from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView,
)

from .views import (
    Login, LogoutView)

urlpatterns = [
    path('login', Login.as_view(), name='auth_client_view'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify', TokenVerifyView.as_view(), name='token_verify'),
    # logout
    path("logout", LogoutView.as_view(), name="logout_clients"),
    
]
