from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rentals.choices import price_choices, bedroom_choices, state_choices

from .models import Rental


def index(request):
    rentals = Rental.objects.order_by("-move_in_date").filter(is_published=True, deposit_down=False)

    paginator = Paginator(rentals, 6)
    page = request.GET.get("page")
    paged_rentals = paginator.get_page(page)

    context = {
        "rentals": paged_rentals,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, "rentals/rentals.html", context)


def rental(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id)

    context = {
        'rental': rental
    }

    return render(request, "rentals/rental.html", context)


def search_rentals(request):
    queryset_list = Rental.objects.order_by('-move_in_date').filter(is_published=True, deposit_down=False)

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
        'rentals': queryset_list,
        'values': request.GET,
    }

    return render(request, "rentals/search_rentals.html", context)
