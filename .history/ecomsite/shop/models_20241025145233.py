from django.db import models

# Create your models here.
class Produts(models.Model):
  titile = models.CharField(max_length=200)
  price = models.FloatField()
  discount_price = models.FloatField()
  category = models.CharField(max_length=200)
  description = models.TextField()
  image = models.CharField(max_length=300)
