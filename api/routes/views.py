from rest_framework import viewsets
from routes.models import Route
from routes.serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
