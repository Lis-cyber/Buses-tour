from django.db import models

# Create your models here.


class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    driver = models.CharField(max_length=500)
    capacity = models.IntegerField()
