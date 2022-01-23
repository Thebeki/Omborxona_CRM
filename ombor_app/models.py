from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    name = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    tur = models.CharField(max_length=40, blank=True)
    number = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.name} ({self.shop_name})"

class Mahsulot(models.Model):
    name = models.CharField(max_length=50)
    brend_name = models.CharField(max_length=50, blank=True)
    kelgan_sum = models.IntegerField()
    sale_sum = models.IntegerField()
    quantity = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.name} ({self.brend_name})"

class Client(models.Model):
    ism = models.CharField(max_length=30, blank=True, verbose_name='ism')
    tel = models.CharField(max_length=30, blank=True, verbose_name='tel')
    shop_name = models.CharField(max_length=30, blank=True, verbose_name='')
    location = models.CharField(max_length=30)
    debt = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} ({self.shop_nomi})"

