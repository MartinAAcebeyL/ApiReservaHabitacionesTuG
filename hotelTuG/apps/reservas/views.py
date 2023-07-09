from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Reserva
from .serializers import ReservaApiSerializer, ReservaSerializer, ReservaActualizarSerializer
from rest_framework.views import APIView
from apps.clientes.models import Cliente


class ReservaListar(generics.ListAPIView):
    """listar todas las reservas de un cliente"""
    serializer_class = ReservaApiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reserva.objects.filter(cliente=user)


class ReservaListarUno(generics.RetrieveAPIView):
    """listar una reserva de un cliente"""
    serializer_class = ReservaApiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reserva.objects.filter(cliente=user)


class ReservaCrear(APIView):
    "reservar una habitacion"
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cliente = Cliente.objects.get(id=request.user.id)
            serializer.save(cliente=cliente)
            habitacion = serializer.validated_data['habitacion']
            habitacion.estado = True
            habitacion.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaActualizar(generics.UpdateAPIView):
    """actualizar una reserva, solo el admin puede hacerlo"""
    serializer_class = ReservaActualizarSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Reserva.objects.all()
