# Generated by Django 3.1.7 on 2021-03-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_auto_20210309_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='parking',
            field=models.CharField(default='On-Street', max_length=20),
            preserve_default=False,
        ),
    ]
