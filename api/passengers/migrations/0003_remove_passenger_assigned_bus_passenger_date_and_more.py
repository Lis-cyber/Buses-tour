# Generated by Django 4.0.6 on 2022-08-12 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_route_assigned_buses'),
        ('passengers', '0002_passenger_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='assigned_bus',
        ),
        migrations.AddField(
            model_name='passenger',
            name='date',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='email',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='routes.route'),
        ),
    ]