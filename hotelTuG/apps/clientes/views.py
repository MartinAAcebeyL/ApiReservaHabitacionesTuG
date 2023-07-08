from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import clientTokenObtainPairSerializer, ClientsApiSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class Login(TokenObtainPairView):
    serializer_class = clientTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        cliente = authenticate(
            email=email,
            password=password
        )

        if cliente:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                return Response({
                    'message': "Login successfully",
                    'success': True,
                    'data': {
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                    }
                }, status=status.HTTP_200_OK)

        return Response({
            'message': "The client with these credentials does not exist",
            'success': False
        }, status=status.HTTP_400_BAD_REQUEST)


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
