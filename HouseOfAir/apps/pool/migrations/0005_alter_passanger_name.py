# Generated by Django 3.2 on 2021-05-16 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0004_auto_20210517_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
    ]