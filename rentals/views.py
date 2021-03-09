from django.shortcuts import render

def index(request):
    return render(request, 'rentals/rentals.html')

def rental(request):
    return render(request, 'rentals/rental.html')

def search(request):
    return render(request, 'rentals/search.html')
