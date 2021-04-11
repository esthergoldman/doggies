from django.contrib import admin

from .models import Pet

class PetAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_published', 'sex', 'arrival_date', 'caretaker','age',)
  list_display_links = ('id', 'name',)
  list_filter = ('caretaker',)
  list_editable = ('is_published',)
  search_fields = ('name', 'description', 'area', 'sex', 'color', 'age',)
  list_per_page = 25

admin.site.register(Pet, PetAdmin)