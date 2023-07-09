from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView,
)

from .views import (
    Login, LogoutView, ClienteListarCrear, 
    ClientActualizarEliminar,)

urlpatterns = [
    #login
    path('login', Login.as_view(), name='auth_client_view'),
    # logout
    path("logout", LogoutView.as_view(), name="logout_clients"),
    # api
    path('', ClienteListarCrear.as_view(), name='cliente-list-create'),
    path('<uuid:pk>', ClientActualizarEliminar.as_view(),
         name='cliente-retrieve-update-destroy'),
]
