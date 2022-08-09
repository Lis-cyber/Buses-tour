from rest_framework import viewsets

from drivers.models import Driver
from drivers.serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
