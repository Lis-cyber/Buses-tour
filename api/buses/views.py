from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from buses.models import Bus
from buses.serializers import BusSerializer

# Create your views here.


@csrf_exempt
def busApi(request, id=0):
    if request.method == "GET":
        buses = Bus.objects.all()
        buses_serializer = BusSerializer(buses, many=True)
        return JsonResponse(buses_serializer.data, safe=False)

    elif request.method == "POST":
        bus_data = JSONParser().parse(request)
        buses_serializer = BusSerializer(data=bus_data)
        if buses_serializer.is_valid():
            buses_serializer.save()
            return JsonResponse("Agregado con Éxito", safe=False)
        return JsonResponse("Ocurrió un error", safe=False)

    elif request.method == "PUT":
        bus_data = JSONParser().parse(request)
        bus = Bus.objects.get(id=bus_data['id'])
        buses_serializer = BusSerializer(bus, data=bus_data)
        if buses_serializer.is_valid():
            buses_serializer.save()
            return JsonResponse("Actualizado con Éxito", safe=False)
        return JsonResponse("Ocurrió un error al actualizar", safe=False)

    elif request.method == "DELETE":
        bus = Bus.objects.get(id=id)
        bus.delete()
        return JsonResponse("Eliminado con Éxito", safe=False)
