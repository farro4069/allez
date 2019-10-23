from django.shortcuts import render, redirect, reverse, get_object_or_404

from carnival.models import Carnival


def index(request):
	event = Carnival.objects.all().last()
	context = {
		'event': event, 

	}
	return render(request,'index.html', context)

