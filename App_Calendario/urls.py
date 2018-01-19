from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CalendarioView, DetalleReunionView

urlpatterns = [
    path('', login_required(CalendarioView.as_view()), name='calendario'),
    path('detalle/<int:id>/', login_required(DetalleReunionView.as_view()), name='detallereunion'),
]