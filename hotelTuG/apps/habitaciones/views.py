from rest_framework import generics
from .models import Habitacion
from .serializers import HabitacionesApiSerializer
from rest_framework.permissions import IsAdminUser


class HabitacionesListar(generics.ListAPIView):
    """listar todas las habitaciones"""
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer


class HabitacionesListarDisponibles(generics.ListAPIView):
    """listar todas las habitaciones disponibles"""
    queryset = Habitacion.objects.filter(estado=False)
    serializer_class = HabitacionesApiSerializer


class HabitacionesListarUno(generics.RetrieveAPIView):
    """listar una habitacion"""
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer


class HabitacionesListarActualizarEliminar(generics.UpdateAPIView, generics.DestroyAPIView):
    """actualizar y eliminar una habitacion, solo para administradores"""
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer
    permission_classes = (IsAdminUser,)


class HabitacionesCrear(generics.CreateAPIView):
    """crear una habitacion, solo para administradores"""
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer
    permission_classes = (IsAdminUser,)
