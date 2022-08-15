from django.db import models
from drivers.models import Driver
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    onRoute = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.driver}'
    
    class Meta:
        ordering = ['id']