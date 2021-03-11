from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Room
from rooms.choices import price_choices, bedroom_choices, state_choices

def index(request):
    rooms = Room.objects.order_by('-move_in_date').filter(is_published=True, deposit_down=False)

    paginator = Paginator(rooms, 6)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)

    context = {
        'rooms': paged_rooms,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'rooms/rooms.html', context)

def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    context = {
        'room': room
    }

    return render(request, 'rooms/room.html', context)

def search_rooms(request):
    queryset_list = Room.objects.order_by('-move_in_date').filter(is_published=True, deposit_down=False)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state_choices[state])
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedroom_choices[bedrooms])

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'rooms': queryset_list,
        'values': request.GET
    }

    return render(request, 'rooms/search_rooms.html', context)

