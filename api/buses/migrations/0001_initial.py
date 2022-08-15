# Generated by Django 4.0.6 on 2022-08-11 17:40

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0002_alter_driver_full_name_alter_driver_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('capacity', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=10)),
                ('driver', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
