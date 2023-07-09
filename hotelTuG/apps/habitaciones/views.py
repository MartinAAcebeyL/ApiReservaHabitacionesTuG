from rest_framework import generics
from .models import Habitacion
from .serializers import HabitacionesApiSerializer
from rest_framework.permissions import IsAdminUser


# listar todas las habitaciones
class HabitacionesListar(generics.ListAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer

# listar todas las habitaciones disponibles
class HabitacionesListarDisponibles(generics.ListAPIView):
    queryset = Habitacion.objects.filter(estado=False)
    serializer_class = HabitacionesApiSerializer


# listar una habitacion
class HabitacionesListarUno(generics.RetrieveAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer

# actualizar y eliminar una habitacion, solo para administradores
class HabitacionesListarActualizarEliminar(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer
    permission_classes = (IsAdminUser,)

# crear una habitacion, solo para administradores
class HabitacionesCrear(generics.CreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer
    permission_classes = (IsAdminUser,)
