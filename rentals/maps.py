import django
import os
import sys
import googlemaps

sys.path.append("W:\Python_Projects\cribs_project")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cribs.settings')
django.setup()

from rentals.models import Rental

gmaps = googlemaps.Client(key='AIzaSyDKlZ22c4XLdg1iLRV9Owxl02N_k9neIJ4')

address = '1726 grove street, #1, ridgewood, NY'

response = gmaps.geocode(address)
print(response[0]['geometry'])
