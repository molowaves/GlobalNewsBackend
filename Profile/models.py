from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	USER_CHOICES =[('r', 'Reader'), ('j', 'Journalist')]
	email = models.EmailField(verbose_name='email', max_length=255, unique=True)
	user_type = models.CharField(max_length=50, choices=USER_CHOICES)

	
	REQUIRED_FIELDS = ['user_type', 'username']
	USERNAME_FIELD = 'email'

class Person(models.Model):
	GENDER_CHOICES = [('M', 'Male'), ('F','Female')]

	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	mname = models.CharField(max_length=100, null=True, blank=True)
	gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
	dob = models.DateField()
	pic = models.ImageField(upload_to='profile_pic', default='default.jpg', null=True, blank=True)
	account = models.OneToOneField(User, on_delete = models.CASCADE)
	class Meta:
		abstract = True

	def __str__(self):
		return self.lname.upper() + " " + self.fname + " " + self.mname

class Reader(Person):
	pass

class Journalist(Person):
	highest_qual = models.CharField(max_length=200, null=True, blank=True)













