from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car
# from .serializers import FilmSerializer

# Create your tests here.
class CarViewsTest(APITestCase):
    def car_get(self):
        r = requests.get('http://127.0.0.1:8000/cars/')
        self.assertEqual(r, '200')
