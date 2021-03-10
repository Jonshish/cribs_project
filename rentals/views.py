from django.shortcuts import render

from .models import Rental

def index(request):
    rentals = Rental.objects.all()

    context = {
        'rentals': rentals
    }

    return render(request, 'rentals/rentals.html', context)

def rental(request, rental_id):
    return render(request, 'rentals/rental.html')

def search(request):
    return render(request, 'rentals/search.html')
