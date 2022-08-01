from django.db import models
from buses.models import Bus
# Create your models here.


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    assigned_seat = models.IntegerField(null=True)
    assigned_bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
