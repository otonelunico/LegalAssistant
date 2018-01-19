from django.urls import path
from .views import CalendarioView, DetalleReunionView

urlpatterns = [
    path('', CalendarioView.as_view(), name='calendario'),
    path('detalle/<int:id>/', DetalleReunionView.as_view(), name='detallereunion'),
]