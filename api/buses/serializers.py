from rest_framework import serializers
from drivers.serializers import DriverSerializer
from drivers.models import Driver
from buses.models import Bus
import json


class BusSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(required=False)
    onRoute = serializers.ReadOnlyField()

    class Meta:
        model = Bus
        fields = '__all__'

    # @staticmethod
    def create(self, cls):
        data = json.loads(json.dumps(cls))
        data["driver"] = Driver.objects.get(name=data["driver"]["name"], last_name=data["driver"]["last_name"])
        bus = Bus.objects.create(**data)
        return bus

    def update(self, instance, validated_data):
        data = json.loads(json.dumps(validated_data.get('driver')))
        instance.name = validated_data.get('name', instance.name)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.driver = Driver.objects.get(name=data["name"], last_name=data["last_name"])
        instance.save()
        return instance
