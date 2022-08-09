from django.db import models
# Create your models here.


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.full_name}'
