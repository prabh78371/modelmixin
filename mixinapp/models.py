from django.db import models

# Create your models here
class Product(models.Model):
    prod_id = models.IntegerField("",default=0)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',blank=True)
