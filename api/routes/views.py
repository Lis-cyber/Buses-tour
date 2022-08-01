from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from routes.models import Route
from routes.serializers import RouteSerializer

# Create your views here.


@csrf_exempt
def routeApi(request, id=0):
    if request.method == "GET":
        routes = Route.objects.all()
        routes_serializer = RouteSerializer(routes, many=True)
        return JsonResponse(routes_serializer.data, safe=False)

    elif request.method == "POST":
        route_data = JSONParser().parse(request)
        routes_serializer = RouteSerializer(data=route_data)
        if routes_serializer.is_valid():
            routes_serializer.save()
            return JsonResponse("Ruta agregada con éxito", safe=False)
        return JsonResponse("Ocurrió un error al agregar la ruta", safe=False)

    elif request.method == "PUT":
        route_data = JSONParser().parse(request)
        route = Route.objects.get(id=route_data['id'])
        routes_serializer = RouteSerializer(
            route, data=route_data)
        if routes_serializer.is_valid():
            routes_serializer.save()
            return JsonResponse("Ruta actualizada con éxito", safe=False)
        return JsonResponse("Ocurrió un error al actualizar la ruta", safe=False)

    elif request.method == "DELETE":
        route = Route.objects.get(id=id)
        route.delete()
        return JsonResponse("Ruta eliminada con éxito", safe=False)
