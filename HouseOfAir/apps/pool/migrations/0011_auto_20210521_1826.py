# Generated by Django 3.2 on 2021-05-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0010_auto_20210521_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='cost_d',
            field=models.PositiveIntegerField(null=True, verbose_name='Суточная стоимость'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='cost_h',
            field=models.PositiveIntegerField(null=True, verbose_name='Почасовая стоимость'),
        ),
    ]
