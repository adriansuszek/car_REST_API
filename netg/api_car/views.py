from django.shortcuts import render
from .models import Car, Rate
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import CarSerializer
from django.views.decorators.csrf import csrf_exempt

# , RateSerializer

# Create your views here.
@csrf_exempt
def car_list(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many = True) #cars is a QuerySet, so: many=UserAttributeSimilarityValidator
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CarSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors, status = 400)


    # try:
    #     cars = Car.objects.get(pk=pk)
    # except Car.DoesNotExist:
    #     return HttpResponse(status=404)
    #
    # if request.method == 'GET':
    #     serializer = CarSerializer(cars, many = True)
    #     return JsonResponse(serializer.data, safe = False)
    #
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = CarSerializer(cars, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     cars.delete()
    #     return HttpResponse(status=204)

@csrf_exempt
def car_detail(request, car_id):

    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car) #cars is a QuerySet, so: many=UserAttributeSimilarityValidator
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car.delete()
        return HttpResponse(status=204)
