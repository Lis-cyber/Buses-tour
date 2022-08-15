from django.db import models
from routes.models import Route
# Create your models here.


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    seat = models.IntegerField(null=True)
    route = models.JSONField()
    
    def __str__(self):
        return f'{self.full_name} {self.seat}'