from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img =  models.ImageField(upload_to='pics')
    desc =  models.TextField(null=True)
    price =  models.DecimalField(max_digits=6, decimal_places=2)
    offer =  models.BooleanField(default=False)
