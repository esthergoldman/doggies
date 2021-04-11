from django.urls import path

from . import views

urlpatterns= [
	path('events',views.events, name='events'),
    path('search_events',views.search_events, name='search_events'),
]
