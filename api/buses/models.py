from django.db import models
from drivers.models import Driver
# Create your models here.


class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.driver}'
    
    class Meta:
        ordering = ['id']