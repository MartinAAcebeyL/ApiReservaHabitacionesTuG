from rest_framework import generics
from .models import Habitacion
from .serializers import HabitacionesApiSerializer
from rest_framework.permissions import IsAuthenticated


class HabitacionesListar(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer


class HabitacionesListarActualizarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionesApiSerializer
    permission_classes = (IsAuthenticated,)