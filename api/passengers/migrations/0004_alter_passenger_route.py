# Generated by Django 4.0.6 on 2022-08-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passengers', '0003_remove_passenger_assigned_bus_passenger_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='route',
            field=models.JSONField(),
        ),
    ]
