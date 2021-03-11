from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="rentals"),
    path("<int:rental_id>", views.rental, name="rental"),
    path("search_rentals", views.search_rentals, name="search_rentals"),
]
