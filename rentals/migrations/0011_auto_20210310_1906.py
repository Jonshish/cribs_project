# Generated by Django 3.1.7 on 2021-03-11 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0010_auto_20210310_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='conceirge',
            new_name='concierge',
        ),
    ]