# Generated by Django 3.2 on 2021-05-16 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0006_auto_20210517_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passanger',
            name='flighе_number',
        ),
        migrations.AddField(
            model_name='passanger',
            name='flight_arrival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pool.arrival_schedule'),
        ),
        migrations.AddField(
            model_name='passanger',
            name='flight_depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pool.depart_schedule'),
        ),
    ]
