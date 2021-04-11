from django.urls import path

from . import views

urlpatterns= [
	path('adopt',views.adopt, name='adopt'),
	path('<int:pet_id>',views.pet, name='pet'),
	path('search', views.search, name='search'),

]

