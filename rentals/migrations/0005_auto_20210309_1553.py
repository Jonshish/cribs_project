# Generated by Django 3.1.7 on 2021-03-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20210309_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='doorman',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rental',
            name='laundry',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rental',
            name='pets_allowed',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rental',
            name='storage',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rental',
            name='valet',
            field=models.CharField(max_length=20),
        ),
    ]