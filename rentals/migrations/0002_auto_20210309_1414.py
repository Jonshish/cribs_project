# Generated by Django 3.1.7 on 2021-03-09 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='move_in_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='rental',
            name='realtor_notes',
            field=models.TextField(blank=True),
        ),
    ]
