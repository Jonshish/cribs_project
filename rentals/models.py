from datetime import datetime
from django.db import models
from realtors.models import Realtor

class Rental(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    backyard = models.BooleanField(blank=True)
    balcony = models.BooleanField(blank=True)
    bathtub = models.BooleanField(blank=True)
    bike_room = models.BooleanField(blank=True)
    bike_storage = models.BooleanField(blank=True)
    pets_allowed = models.CharField(max_length=20)
    central_ac = models.BooleanField(blank=True)
    child_playroom = models.BooleanField(blank=True)
    conceirge = models.BooleanField(blank=True)
    conference_room = models.BooleanField(blank=True)
    dishwasher = models.BooleanField(blank=True)
    doorman = models.CharField(max_length=20)
    elevator = models.BooleanField(blank=True)
    furnished = models.BooleanField(blank=True)
    garden = models.BooleanField(blank=True)
    gym = models.BooleanField(blank=True)
    hardwood_flooring = models.BooleanField(blank=True)
    ice_maker = models.BooleanField(blank=True)
    laundry = models.CharField(max_length=20)
    lobby = models.BooleanField(blank=True)
    microwave = models.BooleanField(blank=True)
    no_fee = models.BooleanField(blank=True)
    shared_outdoor_space = models.BooleanField(blank=True)
    patio = models.BooleanField(blank=True)
    private_outdoor_space = models.BooleanField(blank=True)
    private_rooftop_deck = models.BooleanField(blank=True)
    shared_outdoor_space = models.BooleanField(blank=True)
    stainless_steel_appliances = models.BooleanField(blank=True)
    storage = models.CharField(max_length=20, blank=True)
    swimming_pool = models.BooleanField(blank=True)
    terrace = models.BooleanField(blank=True)
    valet = models.CharField(max_length=20, blank=True)
    rental_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    rental_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    rental_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    deposit_down = models.BooleanField(default=False, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    move_in_date = models.DateField(default=datetime.now)
    realtor_notes = models.TextField(blank=True)
    def __str__(self):
        return self.title