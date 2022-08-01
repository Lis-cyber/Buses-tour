from django.urls import path
from passengers import views

app_name = 'passengers'

urlpatterns = [
    path(r'passengers', views.passengerApi),
    path(r'passengers/<int:id>', views.passengerApi),
]
