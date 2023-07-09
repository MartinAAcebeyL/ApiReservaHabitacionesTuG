from django.urls import path
from .views import (
    Login, LogoutView, ClienteListarCrear,
    ClientActualizarEliminar,)

urlpatterns = [
    # login
    path('login', Login.as_view(), name="login"),
    # logout
    path("logout", LogoutView.as_view(), name="logout"),
    # api
    path('', ClienteListarCrear.as_view(), name='cliente_listar_crear'),
    path('<uuid:pk>', ClientActualizarEliminar.as_view(),
         name='cliente_actualizar_eliminar'),
]
