from django.db import models
from django.contrib.postgres.fields import ArrayField

class Route(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    pax_pct = models.IntegerField(blank=True, null=True)
    pax_num = models.IntegerField(blank=True, null=True)
    assigned_buses = ArrayField(models.JSONField())

    def __str__(self):
        return f'{self.name}'
