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
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    # rate = models.CharField(choices=RATES, max_length=100)
    rate = models.IntegerField(choices=RATES)

    def __str__(self):
        return f'{self.car} rate: {self.rate}'
