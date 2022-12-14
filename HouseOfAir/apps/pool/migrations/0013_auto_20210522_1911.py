# Generated by Django 3.2 on 2021-05-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0012_auto_20210522_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='month_cost',
            field=models.PositiveBigIntegerField(null=True, verbose_name='Стоимость аренды'),
        ),
        migrations.AddField(
            model_name='store',
            name='rent_to',
            field=models.DateField(null=True, verbose_name='Арендовано до'),
        ),
        migrations.AddField(
            model_name='store',
            name='sq_m',
            field=models.PositiveIntegerField(null=True, verbose_name='Квадратных метров'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='store',
            name='tipe',
            field=models.CharField(max_length=10, null=True, verbose_name='Тип магазина'),
        ),
    ]
