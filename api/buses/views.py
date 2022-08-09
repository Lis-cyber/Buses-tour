from rest_framework import viewsets
from buses.models import Bus
from buses.serializers import BusSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
