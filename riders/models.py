from django.db import models
from django.urls import reverse

from accounts.models import MyUser
# from carnival.models import Event


# Create your models here.

class Rider(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	club = models.CharField(max_length=40)
	license_number = models.CharField(max_length=10)
	grade = models.CharField(max_length=10)

	def __str__(self):
		return self.license_number

	def get_absolute_url(self):
		return reverse('rider-detail', kwargs={
			'id': self.id
			})

	@property
	def get_comments(self):
		return self.comments.all().order_by('-timestamp')
    

class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rider = models.ForeignKey(Rider, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




# 	@property
# 	def get_results(self):
# 		return self.Result.all().order_by('-event_date')


# class Result(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     content = models.TextField()
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username