from django.contrib import admin

from .models import Caretaker

class CaretakerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'join_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 5

admin.site.register(Caretaker, CaretakerAdmin)