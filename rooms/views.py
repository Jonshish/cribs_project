from django.shortcuts import render

def index(request):
    return render(request, 'rooms/rooms.html')

def room(request):
    return render(request, 'rooms/room.html')

def search(request):
    return render(request, 'rooms/search.html')

