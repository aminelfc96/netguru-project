from django.db import models


class cars(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    avg_rate = models.FloatField(null=True)

    def __str__(self):
        return f'{self.make} {self.model}'


class rate(models.Model):
    car_id = models.ForeignKey(cars, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rates_number = models.IntegerField(default=0)
    sum_rate = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rating) + ' ' + str(self.car_id.model)

