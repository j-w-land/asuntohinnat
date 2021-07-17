from django.db import models


class Price(models.Model):
    place = models.CharField(max_length=50)
    year = models.IntegerField()
    avgPrice = models.DecimalField(max_digits=10, decimal_places=2)
