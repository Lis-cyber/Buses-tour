from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from drivers.models import Driver
from drivers.serializers import DriverSerializer

# Create your views here.


@csrf_exempt
def driverApi(request, id=0):
    if request.method == "GET":
        drivers = Driver.objects.all()
        drivers_serializer = DriverSerializer(drivers, many=True)
        return JsonResponse(drivers_serializer.data, safe=False)

    elif request.method == "POST":
        driver_data = JSONParser().parse(request)
        drivers_serializer = DriverSerializer(data=driver_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Conductor agregado con éxito", safe=False)
        return JsonResponse("Ocurrió un error al agregar al conductor", safe=False)

    elif request.method == "PUT":
        driver_data = JSONParser().parse(request)
        driver = Driver.objects.get(id=driver_data['id'])
        drivers_serializer = DriverSerializer(driver, data=driver_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Conductor actualizado con éxito", safe=False)
        return JsonResponse("Ocurrió un error al actualizar al conductor", safe=False)

    elif request.method == "DELETE":
        driver = Driver.objects.get(id=id)
        driver.delete()
        return JsonResponse("Conductor eliminado con éxito", safe=False)
