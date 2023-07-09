from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView,
)

from .views import (
    Login, LogoutView, ClienteListarCrear, 
    ClientActualizarEliminar,)

urlpatterns = [
    path('login', Login.as_view(), name='auth_client_view'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify', TokenVerifyView.as_view(), name='token_verify'),
    # logout
    path("logout", LogoutView.as_view(), name="logout_clients"),
    # api
    path('', ClienteListarCrear.as_view(), name='cliente-list-create'),
    path('<uuid:uuid>/', ClientActualizarEliminar.as_view(),
         name='cliente-retrieve-update-destroy'),
]
