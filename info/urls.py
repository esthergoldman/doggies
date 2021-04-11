from django.urls import path

from . import views

urlpatterns= [
	path('',views.index, name='index'),
	path('about',views.about, name='about'),
	path('donate',views.donate, name='donate'),
	path('contact',views.contact, name='contact'),
	path('found',views.add_found, name='found'),
	path('all_found',views.all_found, name='all_found'),

]
