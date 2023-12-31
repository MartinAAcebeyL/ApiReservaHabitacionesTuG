from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from . models import Cliente
from .serializers import clientTokenObtainPairSerializer, ClientsApiSerializer


class Login(TokenObtainPairView):
    serializer_class = clientTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        cliente = authenticate(request, email=email, password=password)
        if cliente is None:
            return Response({
                'message': "Email or password incorrect",
                'success': False
            }, status=status.HTTP_401_UNAUTHORIZED)

        login_serializer = self.serializer_class(data=request.data)
        login_serializer.is_valid(raise_exception=True)

        tokens = {
            'token': login_serializer.validated_data.get('access'),
            'refresh-token': login_serializer.validated_data.get('refresh'),
        }

        return Response({
            'message': "Login successfully",
            'success': True,
            'data': tokens
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'message': "Session ended successfully",
                'success': True
            }, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({
                'message': "An error occurred",
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class ClienteListarCrear(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientsApiSerializer


class ClientActualizarEliminar(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClientsApiSerializer
