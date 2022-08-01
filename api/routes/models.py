from django.db import models
from buses.models import Bus
# Create your models here.


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    assigned_bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(unique=True, null=True, blank=True)
    end_date = models.DateTimeField(unique=True, null=True, blank=True)
    # seat_number = models.IntegerField(null=True)