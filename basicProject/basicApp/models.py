from django.db import models

# Create your models here.
class Book (models.Model):
	#ATTRIBUTES
	title = models.CharField(max_length=40, blank=False)
	author = models.CharField(max_length=20, blank=False)
	pages = models.IntegerField(blank=False)
	
	def __str__(self):
		return self.title