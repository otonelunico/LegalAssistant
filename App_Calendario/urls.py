from django.urls import path
from .views import CalendarioView

urlpatterns = [
    path('', CalendarioView.as_view(), name='calendario'),
]