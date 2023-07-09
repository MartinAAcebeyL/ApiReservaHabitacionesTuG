from django.urls import path
from .views import ReservaListar, ReservaListarUno, ReservaCrear, ReservaActualizar

urlpatterns = [
    path('', ReservaListar.as_view(), name='reserva-listar'),
    path('<int:pk>', ReservaListarUno.as_view(), name='reserva-listar-uno'),
    path('crear/', ReservaCrear.as_view(), name='reserva-crear'),
    path('admin/<int:pk>/', ReservaActualizar.as_view(),
         name='reserva-actualizar'),
]
