from django.db import models

RATES = (
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
)

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.make} {self.model}'

class Rate(models.Model):
    car_id = models.ForeignKey(Car, on_delete = models.CASCADE, null=True) #musze to zmienic na 'car_id'
    rating = models.IntegerField(choices=RATES) #musze to zmienic na 'rating'

    def __str__(self):
        return f'{self.car_id} rate: {self.rate}'
