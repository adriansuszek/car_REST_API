from .models import Car, Rate
import requests
from django.db.models import Count, Avg
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Car, Rate
from .serializers import CarSerializer, RateSerializer, PopularSerializer


@csrf_exempt
def car_list(request):
    if request.method == "GET":
        cars = Car.objects.all()
        avg_rating = Rate.objects.all().values('car_id').annotate(Avg('rating'))


        avg_rate_map = {}
        for avg_rate in avg_rating:
            avg_rate_map[avg_rate['car_id']] = avg_rate['rating__avg']


        for car in cars:
            if car.id in avg_rate_map:
                car.avg_rating = avg_rate_map[car.id]


        serializer = CarSerializer(cars, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":

        data = JSONParser().parse(request)

        car_make = data['make']
        car_model = data['model']

        resp = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{car_make}?format=json')
        external_data = resp.json()


        car_models = []
        for car in external_data['Results']:
            car_models.append(car['Model_Name'].upper())

        if data['model'].upper() in car_models:
            serializer = CarSerializer(data = data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 201)
            else:
                return JsonResponse(serializer.errors, status = 400)
        else:
            return HttpResponse(status=400)

@csrf_exempt
def car_detail(request, car_id):

    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        car.delete()
        return HttpResponse(status=204)


@csrf_exempt
# class CarListView(viewsets.ModelViewSet):
def rates(request):
    if request.method == "GET":
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RateSerializer(data = data)


        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

def popular(request):
    if request.method == "GET":

        cars = Car.objects.all()
        avg_rating = Rate.objects.all().values('car_id').annotate(total=Count('car_id')).order_by('total')

        avg_rate_map = {}
        for avg_rate in avg_rating:
            avg_rate_map[avg_rate['car_id']] = avg_rate['total']


        for car in cars:
            if car.id in avg_rate_map:
                car.rates_number = avg_rate_map[car.id]

        serializer = PopularSerializer(cars, many = True)
        return JsonResponse(serializer.data, safe = False)
