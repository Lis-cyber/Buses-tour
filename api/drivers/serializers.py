from rest_framework import serializers
from drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Driver
        fields = '__all__'

    def create(self, cls):
        cls["full_name"] = cls["name"] + " " + cls["last_name"]
        driver = Driver.objects.create(**cls)
        return driver
