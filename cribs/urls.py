from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("rentals/", include("rentals.urls")),
    path("rooms/", include("rooms.urls")),
    path("admin/", admin.site.urls),
]
