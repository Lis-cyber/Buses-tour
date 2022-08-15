from rest_framework import serializers
from passengers.models import Passenger
from routes.serializers import RouteSerializer
from routes.models import Route
from passengers.models import Passenger
import json


class PassengerSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    route = serializers.ReadOnlyField()
    driver = RouteSerializer(required=False)

    class Meta:
        model = Passenger
        fields = '__all__'

    def create(self, cls):
        data = self.initial_data       
        passenger = Passenger.objects.create(**data)
        return passenger