from django import forms

from .models import Rider, Comment
from accounts.models import MyUser


class RiderForm(forms.ModelForm):
	class Meta:
		model = Rider
		fields = (
			'first_name',
			'last_name',
			'club',
			'license_number',
			'grade'
			)

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Add a new comment',
		'id': 'usercomment',
		'rows': '3',
	}))
	class Meta:
		model = Comment
		fields = ('content', )

