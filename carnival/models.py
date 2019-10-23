from django.db import models

from riders.models import Rider


# Create your models here.

class Racetype(models.Model):
	crit = 'crit'
	road = 'road'
	itt = 'itt'
	ttt = 'ttt'
	hand = 'hand'	
	race_choice = [
		(crit, 'Criterium'),
		(road, 'Road Race'), 
		(itt, 'ITT'), 
		(ttt, 'TTT'), 
		(hand, 'Handicap'),
	]
	race_type = models.CharField(
		max_length=9, 
		choices=race_choice, 
		default=crit,
	)

	def __str__(self):
		return self.race_type

class Place(models.Model):
	place = models.CharField(max_length=4, default=8)

	def __str__(self):
		return self.place

class Grade(models.Model):
	title = models.CharField(max_length=12)

	def __str__(self):
		return self.title

class Carnival(models.Model):
	date = models.DateField(default='2020-01-01')
	description = models.CharField(max_length=120)
	# race_type = models.ForeignKey(Racetype, null=True, on_delete=models.CASCADE)
	categories = models.ManyToManyField(Grade)

	def __str__(self):
		return self.description

	@property
	def get_categories(self):
		return self.categories.all()
    

class Register(models.Model):
	event = models.ForeignKey(Carnival, on_delete=models.CASCADE)
	bib = models.CharField(max_length=3)
	rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
	race = models.ForeignKey(Grade, on_delete=models.CASCADE)
	prime_one = models.BooleanField(default=False)
	prime_two = models.BooleanField(default=False)
	prime_three = models.BooleanField(default=False)
	result = models.ForeignKey(Place, on_delete=models.CASCADE)
	start_time = models.TimeField(default='0:00:00')
	finish_time = models.TimeField(default='0:00:00')

	def __str__(self):
		return self.bib
