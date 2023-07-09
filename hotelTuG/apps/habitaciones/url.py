from django.urls import path

from .views import (HabitacionesListar, HabitacionesListarActualizarEliminar)

urlpatterns = [
    path('habitaciones/', HabitacionesListar.as_view(), name='habitaciones'),
    
    path('habitaciones/<int:pk>/', HabitacionesListarActualizarEliminar.as_view(), name='habitaciones'),
]