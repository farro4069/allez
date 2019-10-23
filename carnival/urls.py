from django.contrib import admin
from django.urls import path, include
from allez.views import index
from carnival.views import (
	carnival, 
	create_carnival, 
	prime_one,
	prime_two,
	prime_three,
	registration, 
	registration2,
	results,
	result_update,
	start_list, 
	starter_detail,
	starter_delete,
	)

urlpatterns = [
    path('', carnival, name='carnival'),
    path('add/', create_carnival, name='add-carnival'),
    path('registration/', registration, name='registration'),
    path('registration2/', registration2, name='registration2'),
    path('results/<ev>/<ra>/', results, name='results'),
    path('result/<pk>/update/', result_update, name='result-update'),
    path('starter/<pk>/update/', starter_detail, name='starter-detail'),
    path('starter/<pk>/delete/', starter_delete, name='starter-delete'),
    path('starters/<ra>/', start_list, name='start-list'),
    path('starters/', start_list, name='start-list'),
    path('result/<ev>/<ra>/<pk>/prime_one/', prime_one, name='prime-one'),
    path('result/<ev>/<ra>/<pk>/prime_two/', prime_two, name='prime-two'),
    path('result/<ev>/<ra>/<pk>/prime_three/', prime_three, name='prime-three'),


]


