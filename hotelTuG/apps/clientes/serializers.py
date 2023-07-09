from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import Cliente

class clientTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class ClientsApiSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = []
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        print(validated_data)
        cliente = Cliente(**validated_data)
        cliente.save()
        return cliente