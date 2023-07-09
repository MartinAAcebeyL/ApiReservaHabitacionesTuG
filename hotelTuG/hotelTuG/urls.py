from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/clientes/', include('apps.clientes.urls')),
    path('api/v1/habitaciones/', include('apps.habitaciones.urls')),
    path('api/v1/reservas/', include('apps.reservas.urls')),
]
