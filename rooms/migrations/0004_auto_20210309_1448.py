# Generated by Django 3.1.7 on 2021-03-09 19:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_deposit_down'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='laundry',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('in_building', 'In Building'), ('in_unit', 'In Unit')], default=[], size=None),
        ),
    ]
