from rest_framework import serializers
from .models import Reserva


class ReservaApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = []


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['cliente', 'estado']

    def validate(self, data):
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        monto_pagado = data.get('monto')
        habitacion = data.get('habitacion')

        if fecha_inicio >= fecha_fin:
            raise serializers.ValidationError(
                "La fecha de fin debe ser posterior a la fecha de inicio.")

        if monto_pagado == habitacion.precio:
            data['estado'] = 'Pa'
        elif monto_pagado < habitacion.precio:
            data['estado'] = 'P'
        else:
            raise serializers.ValidationError(
                "El monto pagado no puede ser mayor al precio de la habitación.")
        
        if habitacion.estado:
            raise serializers.ValidationError(
                "La habitación no está disponible.")
        
        reservas_chocantes = Reserva.objects.filter(
            habitacion=habitacion, fecha_inicio__lt=fecha_fin, fecha_fin__gt=fecha_inicio)
        if reservas_chocantes.exists():
            raise serializers.ValidationError(
                "Las fechas de reserva chocan con una reserva existente.")

        return data


class ReservaActualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['cliente', 'fecha_inicio',
                            'fecha_fin', 'fecha_registro']
