from rest_framework.serializers import ModelSerializer
from .models import Habitacion


class HabitacionesApiSerializer(ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        read_only_fields = []
