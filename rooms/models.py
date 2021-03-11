from datetime import datetime
from django.db import models
from realtors.models import Realtor

class Room(models.Model):
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
    bedroom_sqft = models.CharField(max_length=20)
    backyard = models.BooleanField(blank=True)
    balcony = models.BooleanField(blank=True)
    bathtub = models.BooleanField(blank=True)
    bike_room = models.BooleanField(blank=True)
    bike_storage = models.BooleanField(blank=True)
    pets_allowed = models.CharField(max_length=20)
    central_ac = models.BooleanField(blank=True)
    child_playroom = models.BooleanField(blank=True)
    concierge = models.BooleanField(blank=True)
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
    broker_fee = models.CharField(max_length=20)
    parking = models.CharField(max_length=20)
    patio = models.BooleanField(blank=True)
    private_outdoor_space = models.BooleanField(blank=True)
    private_rooftop_deck = models.BooleanField(blank=True)
    shared_outdoor_space = models.BooleanField(blank=True)
    stainless_steel_appliances = models.BooleanField(blank=True)
    storage = models.CharField(max_length=20, blank=True)
    swimming_pool = models.BooleanField(blank=True)
    terrace = models.BooleanField(blank=True)
    valet = models.CharField(max_length=20)
    room_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    room_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    room_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    deposit_down = models.BooleanField(default=False, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    move_in_date = models.DateField(default=datetime.now)
    realtor_notes = models.TextField(blank=True)
    def __str__(self):
        return self.title
