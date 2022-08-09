from rest_framework import viewsets
from passengers.models import Passenger
from passengers.serializers import PassengerSerializer

# Create your views here.


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
