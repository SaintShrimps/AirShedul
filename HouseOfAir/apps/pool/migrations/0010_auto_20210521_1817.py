# Generated by Django 3.2 on 2021-05-21 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0009_auto_20210517_1558'),
    ]

    operations = [
        migrations.DeleteModel(
            name='deleted_schedule',
        ),
        migrations.RenameField(
            model_name='depart_schedule',
            old_name='from_where',
            new_name='where',
        ),
    ]