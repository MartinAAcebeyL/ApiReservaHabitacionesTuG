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
    serializer_class = HabitacionesApiSerializer

    def get_queryset(self):
        queryset = Habitacion.objects.filter(estado=False)

        precio_max = self.request.query_params.get('precio_max', None)
        tipos = self.request.query_params.getlist('tipo[]')
        
        if precio_max is not None:
            queryset = queryset.filter(precio__lte=precio_max)
        if tipos:
            queryset = queryset.filter(tipo__in=tipos)
        return queryset


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
