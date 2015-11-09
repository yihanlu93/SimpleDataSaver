from django.db import models

# Create your models here.

class data(models.Model):

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	name = models.CharField(max_length = 30)
	sex = models.CharField(max_length = 6, choices = GENDER_CHOICES)
	age = models.IntegerField()
	active = models.BooleanField()
	tags = models.TextField()

	def __unicode__(self):
		return self.name

class tag(models.Model):
	GROUP_CHOICES = (
			('K', 'KIDS'),
			('A', 'ADULT'),
			('S', 'SENIOR')
		)

	person = models.OneToOneField(data,related_name='personModel', primary_key=True)
	age_group = models.CharField(max_length = 6, choices = GROUP_CHOICES)

	def __unicode__(self):
		return self.person