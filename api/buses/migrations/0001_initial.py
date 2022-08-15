# Generated by Django 4.0.6 on 2022-08-15 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('onRoute', models.BooleanField(default=False)),
                ('driver', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
