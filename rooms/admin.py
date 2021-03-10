from django.contrib import admin

from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'city',
        'price',
        'bedrooms',
        'move_in_date',
        'deposit_down',
        'is_published',
        'realtor',
        
    )
    list_display_links = ('id', 'title')
    list_filter = ('title', 'city', 'price', 'bedrooms', 'realtor')
    list_editable = ('is_published', 'deposit_down')
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price', 'bedrooms', 'move_in_date')
    list_per_page = 25


admin.site.register(Room, RoomAdmin)