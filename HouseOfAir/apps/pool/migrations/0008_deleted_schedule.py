# Generated by Django 3.2 on 2021-05-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0007_auto_20210517_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='deleted_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_or_arr', models.BooleanField(null=True, verbose_name='Вылетел/Прилител')),
                ('arrival_time', models.DateTimeField(verbose_name='Время')),
                ('from_where', models.CharField(max_length=25, verbose_name='Город вылета/Город прилета')),
                ('company', models.CharField(max_length=25, verbose_name='Название компании')),
                ('plain', models.CharField(max_length=25, verbose_name='Самолет')),
                ('terminal', models.CharField(max_length=5, verbose_name='Терминал')),
                ('dispatcher', models.CharField(max_length=255, verbose_name='Диспетчер')),
            ],
        ),
    ]
