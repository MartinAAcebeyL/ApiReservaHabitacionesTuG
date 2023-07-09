from django.urls import path

from .views import ReservasView

urlpatterns = [
    path('', ReservasView.as_view(), name='reservas'),
]