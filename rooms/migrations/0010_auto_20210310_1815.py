# Generated by Django 3.1.7 on 2021-03-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_room_parking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='no_fee',
        ),
        migrations.AddField(
            model_name='room',
            name='broker_fee',
            field=models.IntegerField(default='2300'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='valet',
            field=models.CharField(max_length=20),
        ),
    ]
