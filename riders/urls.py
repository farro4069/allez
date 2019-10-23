from django.contrib import admin
from django.urls import path, include

from riders.views import add_rider, rider_list, rider_detail, rider_update, search


urlpatterns = [
	path('add/', add_rider, name='add-rider'),
	path('list/', rider_list, name='rider-list'),
	path('rider/<id>/', rider_detail, name='rider-detail'),
    path('rider/<id>/update/', rider_update, name='rider-update'),	
    path('search/', search, name='search'),


]
