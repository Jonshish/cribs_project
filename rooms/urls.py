from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="rooms"),
    path("<int:room_id>", views.room, name="room"),
    path("rooms/search>", views.search, name="search"),
]
