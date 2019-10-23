from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth import get_user_model, login, logout


from .forms import UserCreationForm, UserLoginForm
from carnival.models import Carnival


def register(request, **kwargs):
	event = Carnival.objects.all().last()
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('login'))

	context = {
		'event': event,
		'form': form,
	}
	return render(request, 'accounts/register.html', context)


def login_view(request, *args, **kwargs):
	event = Carnival.objects.all().last()
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		login(request, user_obj)
		return redirect(reverse('index'))

	context= {
		'event': event,
		'form': form,
	}
	return render(request, 'accounts/login.html', context)

def logout_view(request):
	logout(request)
	return redirect(reverse('index'))

