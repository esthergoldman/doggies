from django.contrib import admin

from info.models import Contact
from info.models import Found

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'contact_date')
    search_fields = ('first_name', 'email', 'contact_date')
    list_per_page = 20



admin.site.register(Contact, ContactAdmin)


class FoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'name', 'city')
    search_fields = ('name', 'location', 'city')
    list_per_page = 20
admin.site.register(Found, FoundAdmin)