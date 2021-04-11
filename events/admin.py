from django.contrib import admin
from .models import Location
from .models import Event




class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')    
    ordering = ('name',)


admin.site.register(Location, LocationAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date','organizer','location',)
    search_fields = ('name', 'event_date',)
    list_per_page = 20
    list_filter =('event_date', 'location', 'name')
    ordering = ('-event_date',)

admin.site.register(Event, EventAdmin)