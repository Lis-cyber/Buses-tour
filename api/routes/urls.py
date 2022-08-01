from django.urls import path
from routes import views

app_name = 'routes'

urlpatterns = [
    path(r'routes', views.routeApi),
    path(r'routes/<int:id>', views.routeApi),
]
