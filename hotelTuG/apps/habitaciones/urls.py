from django.urls import path

from .views import (HabitacionesListar, HabitacionesListarUno,
                    HabitacionesListarActualizarEliminar, HabitacionesCrear,
                    HabitacionesListarDisponibles)

urlpatterns = [
    path('', HabitacionesListar.as_view(), name='listar-habitaciones'),
    path('disponibles', HabitacionesListarDisponibles.as_view(),
         name='listar-habitaciones-disponibles'),
    path('<int:pk>', HabitacionesListarUno.as_view(),
         name='listar-una-habitaciones'),
    path('admin/<int:pk>/',
         HabitacionesListarActualizarEliminar.as_view(), name='actualizar-eliminar-habitacion'),
    path('admin/crear/', HabitacionesCrear.as_view(), name='crear-habitaciones'),
]
