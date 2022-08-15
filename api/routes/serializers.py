from rest_framework import serializers
from routes.models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

    def create(self, cls):
        data = self.initial_data
        route = Route.objects.create(**data)
        return route