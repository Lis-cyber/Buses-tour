# Generated by Django 4.0.6 on 2022-08-01 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buses', '0002_alter_bus_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(blank=True, null=True, unique=True)),
                ('end_date', models.DateTimeField(blank=True, null=True, unique=True)),
                ('assigned_bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buses.bus')),
            ],
        ),
    ]
