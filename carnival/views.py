from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.db.models import Q

from riders.models import Rider
from .models import Carnival, Register, Grade, Place
from .forms import RegisterForm, CarnivalForm, ResultForm


def carnival(request):
	history = Carnival.objects.all().order_by('-date')
	event = Carnival.objects.all().last()
	context = {
		'history': history,
		'event': event,
	}
	return render(request,'carnival/carnival.html', context)


def create_carnival(request):
	if request.method == 'POST':
		form = CarnivalForm(request.POST)
		if form.is_valid():
			form.save()
		event = Carnival.objects.all().last()
		context = {
			'event': event, 
			}
		return render(request, 'carnival/carnival.html', context)
	event = Carnival.objects.all().last()
	form = CarnivalForm()
	context = {
		'form': form,
		'event': event,
	}
	return render(request, 'carnival/carnival_create.html', context)


def get_grade(event):
	races = []
	queryset = Register.objects.\
	filter(event=event)\
	.values_list('race', flat=True)\
	.distinct()
	for qs in queryset:
		race = Grade.objects.get(id=qs)
		races.append(race)
	print(races)
	return races

def start_list(request, ra):
	event = Carnival.objects.all().order_by('date').last()
	races = get_grade(event)
	if ra == "0": 
		starters = Register.objects\
		.filter(event=event)\
		.extra(select={'bib_number': 'CAST(bib AS INTEGER)'})\
		.order_by('race', 'bib_number')
		race_name = 'All categories'
	else:
		starters = Register.objects.\
		filter(event=event, race=ra)\
		.extra(select={'bib_number': 'CAST(bib AS INTEGER)'})\
		.order_by('bib_number')
		race_name = Grade.objects.filter(id=ra).last()
	number_starters = starters.count()
	context = {
		'event': event,
		'starters': starters,
		'races': races,
		'race_name': race_name,
		'number_starters': number_starters,
	}
	return render(request,'carnival/start_list.html', context)


def registration(request):
	recents = Register.objects.all().order_by('-id')[:5]
	event = Carnival.objects.all().order_by('date').last()

	context = {
		'event': event,
		'recents': recents,
	}
	return render(request,'carnival/registration.html', context)

def registration2(request, *args, **kwargs):
	recents = Register.objects.all().order_by('-id')[:5]
	event = Carnival.objects.all().order_by('date').last()
	races = get_grade(event)
	if request.method == 'POST':

		form = RegisterForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
		context = {
			'event': event,
			'recents': recents,
			'races': races,
		}
		return render(request, 'carnival/registration.html', context)

	else: 
		query = request.GET.get('q')
		result = get_object_or_404(Place, id=8)
		if query:
			rider = Rider.objects.filter(Q(license_number__iexact=query)).first()
			form = RegisterForm(initial = {'rider': rider, 'event': event, 'result': result})
			context = {
				'recents': recents,
				'event': event,
				'rider': rider,
				'races': races,
				'form': form,
			}
			return render(request,'carnival/registration2.html', context)

		else:
			if request.id:
				rider = Rider.objects.get_object_or_404(id=request.id)
				context = {
					'recents': recents,
					'event': event,
					'rider': rider,
					'races': races, 

				}
				return render(request,'carnival/registration2.html', context)

			else:
				context = {
					'recents': recents,
					'event': event,
					'rider': rider,
					'races': races, 
				}
				return render(request,'carnival/registration.html', context)


def starter_detail(request, pk):
	event = Carnival.objects.all().order_by('date').last()
	recents = Register.objects.all().order_by('-id')[:5]
	starter = get_object_or_404(Register, id=pk)
	rider = get_object_or_404(Rider, license_number=starter.rider)
	form = RegisterForm(request.POST or None, instance=starter)
	if request.method == 'POST':
		if form.is_valid():
			form.save()

		context = {
			'event': event,
			'recents': recents,
		}
		ra = starter.race.id

		return redirect(reverse('start-list', kwargs={'ra': ra}))
		# return render(request, 'carnival/registration.html', context)
	context = {
		'event': event,
		'recents': recents,
		'rider': rider,
		'form': form,
	}
	return render(request, 'carnival/registration2.html', context)

def starter_delete(request, pk):
	event = Carnival.objects.all().order_by('date').last()
	starter = get_object_or_404(Register, id=pk)
	ra = starter.race.id
	starter.delete()
	context = {
		'event': event,
	}

	return redirect(reverse('start-list', kwargs={'ra': ra}))


def result_update(request, pk):
	event = Carnival.objects.all().order_by('date').last()
	races = get_grade(event)
	starters = Register.objects.\
	filter(event=event, race=pk)\
	.extra(select={'bib_number': 'CAST(bib AS INTEGER)'})\
	.order_by('result','bib_number')
	race_name = Grade.objects.filter(id=pk).last()
	number_starters = starters.count()

	if request.method == 'POST':
		starter = get_object_or_404(Register, id=pk)
		form = ResultForm(request.POST, instance=starter)
		if form.is_valid():
			form.save()

		context = {
			'event': event,
			'starters': starters,
			'races': races,
			'race_name': race_name,
			'number_starters': number_starters,
 
		}
		ev=event.id
		ra=starter.race.id

		return redirect(reverse('results', kwargs={'ev': ev, 'ra': ra}))

	starter = get_object_or_404(Register, id=pk)
	form = ResultForm(request.POST or None, instance=starter)
		
	context = {
		'event': event,
		'starter': starter,
		'form': form,
	}			
	return render(request, 'carnival/result_update.html', context)


def results(request, ev, ra):
	event = get_object_or_404(Carnival, id=ev)
	races = get_grade(event)
	if ra == "0": 
		starters = Register.objects\
		.filter(event=event)\
		.extra(select={'bib_number': 'CAST(bib AS INTEGER)'})\
		.order_by('race', 'result', '-prime_one', 'bib_number')
		race_name = 'All categories'
	else:
		starters = Register.objects.\
		filter(event=event, race=ra)\
		.extra(select={'bib_number': 'CAST(bib AS INTEGER)'})\
		.order_by('result', '-prime_one', '-prime_two', '-prime_three', 'bib_number')
		race_name = get_object_or_404(Grade, id=ra)
	number_starters = starters.count()

	context = {
		'event': event,
		'starters': starters,
		'races': races,
		'race_name': race_name,
		'number_starters': number_starters,
	}		
	return render(request, 'carnival/results.html', context)

def prime_one(request, ev, ra, pk):
	prime = get_object_or_404(Register, id=pk)
	if prime.prime_one:
		prime.prime_one = False
		prime.save()
	else:
		prime.prime_one = True
		prime.save()
	return redirect(reverse('results', kwargs={'ev': ev, 'ra': ra}))

def prime_two(request, ev, ra, pk):
	prime = get_object_or_404(Register, id=pk)
	if prime.prime_two:
		prime.prime_two = False
		prime.save()
	else:
		prime.prime_two = True
		prime.save()
	return redirect(reverse('results', kwargs={'ev': ev, 'ra': ra}))

def prime_three(request, ev, ra, pk):
	prime = get_object_or_404(Register, id=pk)
	if prime.prime_three:
		prime.prime_three = False
		prime.save()
	else:
		prime.prime_three = True
		prime.save()
	return redirect(reverse('results', kwargs={'ev': ev, 'ra': ra}))

