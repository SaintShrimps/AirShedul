# Generated by Django 3.2 on 2021-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0002_alter_parking_tipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='tipe',
            field=models.CharField(max_length=15, verbose_name='Тип парковки'),
        ),
    ]
