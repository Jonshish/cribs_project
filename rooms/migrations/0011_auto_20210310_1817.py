# Generated by Django 3.1.7 on 2021-03-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20210310_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='broker_fee',
            field=models.CharField(max_length=20),
        ),
    ]
