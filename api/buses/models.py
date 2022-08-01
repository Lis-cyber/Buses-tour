from django.db import models
from drivers.models import Driver
# Create your models here.


class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    capacity = models.IntegerField()
