from django.db import models
from ombor_app.models import *

class Stats(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    quantity = models.PositiveSmallIntegerField()
    max_summa = models.IntegerField()
    tolandi = models.IntegerField()
    nasiya = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.client.ism}, {self.product.name} ({self.quantity}), {self.date} "

