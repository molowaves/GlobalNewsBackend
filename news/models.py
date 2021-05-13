from django.db import models
from Profile.models import Journalist


class Article(models.Model):
	CATEGORY_CHOICES = [
		('p', 'Politics'),
		('s', 'Sports'),
		('h', 'Health'),
		('t', 'Technology'),
		('e', 'Arts and Entertainment')
	]
	title = models.CharField(max_length=200)
	story = models.TextField()
	pic = models.ImageField(upload_to="news_pics", default='default.jpg')
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Journalist, on_delete=models.CASCADE)
	category = models.CharField(max_length=50, choices = CATEGORY_CHOICES, default='p')
	published = models.BooleanField(default=False)

	def __str__(self):
		return self.title.upper() + "-" + self.date_posted.lower()




class Comment(models.Model):
	comment = models.TextField()
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add=True)
	# author = models.ForeignKey(J)

	def __str__(self):
		return self.comment

