from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rentals.choices import price_choices, bedroom_choices, state_choices

from .models import Rental


def index(request):
    rentals = Rental.objects.order_by("-move_in_date").filter(is_published=True)

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
    return render(request, "rentals/search_rentals.html")
