from django.contrib import admin

from .models import roomContact

class roomContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'room')
    list_per_page = 25


admin.site.register(roomContact, roomContactAdmin)
