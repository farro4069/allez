from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Rider, Comment
from carnival.models import Carnival, Register
from .forms import CommentForm, RiderForm


# Create your views here.

def rider_list(request):
	event = Carnival.objects.all().last()
	riders = Rider.objects.all().order_by('license_number')
	paginator = Paginator(riders, 30)
	page_request_var = 'page'
	page = request.GET.get('page')
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		'event': event,
		'riders': paginated_queryset,
		'page_request_var': page_request_var,
	}

	return render(request, 'riders/rider_list.html', context)

def rider_detail(request, id):
	event = Carnival.objects.all().last()
	rider = get_object_or_404(Rider, id=id)
	history = Register.objects.filter(rider=rider).order_by('-event')
	form = CommentForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.instance.user = request.user
			form.instance.rider = rider
			form.save()
			return redirect(reverse('rider-detail', kwargs={
				'id': rider.pk
				}))
	context = {
		'event': event,
		'form': form,
		'rider': rider,
		'history': history,
	}
	return render(request, 'riders/rider_detail.html', context)
	

def search(request):
	event = Carnival.objects.all().last()
	queryset = Rider.objects.all()
	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query) |
			Q(license_number__icontains=query)
		).distinct().order_by('last_name')
	context = {
		'event': event, 
		'queryset': queryset,
	}
	return render(request, 'riders/search_results.html', context)

def add_rider(request):
	event = Carnival.objects.all().last()
	title = 'Add'
	form = RiderForm(request.POST or None, request.FILES or None)
	user = request.user
	if request.method == "POST":
		if form.is_valid():
			form.instance.user = user
			form.save()
			return redirect(reverse('rider-detail', kwargs={
				'id': form.instance.id,
			}))
	context = {
		'event': event, 
		'title': title,
		'form': form,
	}
	return render(request, 'riders/add_rider.html', context)

def rider_update(request, id):
	event = Carnival.objects.all().last()
	title = 'Update'
	rider = get_object_or_404(Rider, id=id)
	form = RiderForm(
		request.POST or None, 
		request.FILES or None, 
		instance=rider
		)
	user = request.user
	if request.method == "POST":
		if form.is_valid():
			form.instance.user = user
			form.save()
			return redirect(reverse('rider-detail', kwargs={
				'id': form.instance.id,
			}))
	context = {
		'event': event, 
		'title': title,
		'form': form,
	}
	return render(request, 'riders/add_rider.html', context)
