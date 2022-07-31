from django.urls import path
from drivers import views

app_name = 'drivers'

urlpatterns = [
    path(r'drivers', views.driverApi),
    path(r'drivers/<int:id>', views.driverApi),
]
