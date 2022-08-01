from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from passengers.models import Passenger
from passengers.serializers import PassengerSerializer

# Create your views here.


@csrf_exempt
def passengerApi(request, id=0):
    if request.method == "GET":
        passengers = Passenger.objects.all()
        passengers_serializer = PassengerSerializer(passengers, many=True)
        return JsonResponse(passengers_serializer.data, safe=False)

    elif request.method == "POST":
        passenger_data = JSONParser().parse(request)
        passengers_serializer = PassengerSerializer(data=passenger_data)
        if passengers_serializer.is_valid():
            passengers_serializer.save()
            return JsonResponse("Pasajero agregado con éxito", safe=False)
        return JsonResponse("Ocurrió un error al agregar al pasajero", safe=False)

    elif request.method == "PUT":
        passenger_data = JSONParser().parse(request)
        passenger = Passenger.objects.get(id=passenger_data['id'])
        passengers_serializer = PassengerSerializer(
            passenger, data=passenger_data)
        if passengers_serializer.is_valid():
            passengers_serializer.save()
            return JsonResponse("Pasajero actualizado con éxito", safe=False)
        return JsonResponse("Ocurrió un error al actualizar al pasajero", safe=False)

    elif request.method == "DELETE":
        passenger = Passenger.objects.get(id=id)
        passenger.delete()
        return JsonResponse("Pasajero eliminado con éxito", safe=False)
