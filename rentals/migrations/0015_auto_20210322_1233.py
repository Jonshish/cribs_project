# Generated by Django 3.1.7 on 2021-03-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0014_auto_20210322_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='lat',
            field=models.DecimalField(decimal_places=6, help_text='Go to https://www.google.com/maps and search your apartments address. Right-click on the pointer and copy your lat and lng values', max_digits=9),
        ),
        migrations.AlterField(
            model_name='rental',
            name='lng',
            field=models.DecimalField(decimal_places=6, help_text='Go to https://www.google.com/maps and search your apartments address. Right-click on the pointer and copy your lat and lng values', max_digits=9),
        ),
    ]
