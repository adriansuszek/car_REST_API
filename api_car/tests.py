import json

from rest_framework.test import APITestCase

from .models import Car, Rate


# Create your tests here.
class CarPostTestCase(APITestCase):
    def test_car_post(self):
        data = {"make" : "HONDA", "model" : "Civic"}
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_car_post_failed(self):
        data = {"make" : "HONDA", "model" : "asdzxcas"}
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, 400)


class CarGetPositiveCase(APITestCase):
    def test_car_get(self):
        car = Car.objects.create(make="HONDA", model="Civic")
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, 200)
        expected_data = [{'avg_rating': None, 'id': car.id, 'make': 'HONDA', 'model': 'Civic'}]
        self.assertEqual(json.loads(response.content), expected_data)


class CarGetPopularPositiveCase(APITestCase):
    def test_car_get_popular(self):
        car = Car.objects.create(make="HONDA", model="Civic")
        Rate.objects.create(car_id = car, rate=5)
        response = self.client.get("/popular/")
        self.assertEqual(response.status_code, 200)
        expected_data = [{'id': car.id, 'make': 'HONDA', 'model': 'Civic', 'rates_number': 1}]
        self.assertEqual(json.loads(response.content), expected_data)


class RatePostPositiveTestCase(APITestCase):
    def test_rate_post(self):
        car = Car.objects.create(make="HONDA", model="Civic")

        data = {"car_id" : car.id, "rate" : 5}
        response = self.client.post("/rate/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content), data)


class CarDeletePositiveTestCase(APITestCase):
    def test_car_delete(self):
        car_to_delete = Car.objects.create(make="HONDA", model="Civic")
        response = self.client.delete(f"/cars/{car_to_delete.id}")
        self.assertEqual(response.status_code, 204)
