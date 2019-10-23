from django import forms
from django.contrib import admin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Field, Fieldset, Layout, Submit

from .models import Carnival, Grade, Place, Racetype, Register


class CarnivalForm(forms.ModelForm):
	categories = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple(), 
		queryset=Grade.objects.all()
		)
	class Meta:
		model = Carnival
		fields = (
			'date',
			'description',
			'categories',
			)
	def __init__(self, *args, **kwargs):
		super(CarnivalForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('date', css_class='my-form'),
			Field('description', css_class='my-form'),
			Field('categories', css_class=''),
			ButtonHolder(
				Submit('submit', 'Submit', css_class='button'))
			)

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Register
		fields = (
			'event',
			'rider',
			'race',
			'bib',
			'result',
			)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('race', css_class='my-form'),
			Field('bib', css_class='my-form'),
			Field('event', type='hidden'),
			Field('rider', type='hidden'),
			Field('result', type='hidden'),
			ButtonHolder(
				Submit('submit', 'Register', css_class='button'))
			)

class ResultForm(forms.ModelForm):
	current_event = Carnival.objects.all().last()

	class Meta:
		model = Register
		fields = (
			'event',
			'race',
			'bib',
			'rider',
			'result',
			)

	def __init__(self, *args, **kwargs):
		super(ResultForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Fieldset(
				'Result Details',
				'result',
			),
			Field('event', type='hidden'),
			Field('race', type='hidden'),
			Field('rider', type='hidden'),
			Field('bib', type='hidden'),

			ButtonHolder(
				Submit('submit', 'Record', css_class='button'))
			)
