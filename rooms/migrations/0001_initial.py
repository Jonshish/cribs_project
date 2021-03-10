# Generated by Django 3.1.7 on 2021-03-09 18:33

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sqft', models.IntegerField()),
                ('backyard', models.BooleanField(blank=True)),
                ('balcony', models.BooleanField(blank=True)),
                ('bathtub', models.BooleanField(blank=True)),
                ('bike_room', models.BooleanField(blank=True)),
                ('bike_storage', models.BooleanField(blank=True)),
                ('pets_allowed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('cats', 'Cats')], size=None)),
                ('central_ac', models.BooleanField(blank=True)),
                ('child_playroom', models.BooleanField(blank=True)),
                ('conceirge', models.BooleanField(blank=True)),
                ('conference_room', models.BooleanField(blank=True)),
                ('dishwasher', models.BooleanField(blank=True)),
                ('doorman', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('virtual', 'Virtual')], size=None)),
                ('elevator', models.BooleanField(blank=True)),
                ('furnished', models.BooleanField(blank=True)),
                ('garden', models.BooleanField(blank=True)),
                ('gym', models.BooleanField(blank=True)),
                ('hardwood_flooring', models.BooleanField(blank=True)),
                ('ice_maker', models.BooleanField(blank=True)),
                ('laundry', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('in_building', 'In Building'), ('in_unit', 'In Unit')], size=None)),
                ('lobby', models.BooleanField(blank=True)),
                ('microwave', models.BooleanField(blank=True)),
                ('no_fee', models.BooleanField(blank=True)),
                ('patio', models.BooleanField(blank=True)),
                ('private_outdoor_space', models.BooleanField(blank=True)),
                ('private_rooftop_deck', models.BooleanField(blank=True)),
                ('shared_outdoor_space', models.BooleanField(blank=True)),
                ('stainless_steel_appliances', models.BooleanField(blank=True)),
                ('storage', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('private', 'Private'), ('shared', 'Shared'), ('yes', 'Yes'), ('no', 'No')], size=None)),
                ('swimming_pool', models.BooleanField(blank=True)),
                ('terrace', models.BooleanField(blank=True)),
                ('valet', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, choices=[('dry_cleaning', 'Dry Cleaning'), ('parking', 'Parking'), ('yes', 'Yes')], size=None)),
                ('room_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('room_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_11', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('room_12', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
