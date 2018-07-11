from django.db import models

# Create your models here.
class Book (models.Model):
	#ATTRIBUTES
	title = models.CharField(max_length=40, blank=False)
	author = models.CharField(max_length=20, blank=False)
	pages = models.IntegerField(blank=False)
	
	def __str__(self):
		return self.title

class Product (models.Model):
	#ATTRIBUTES
	name = models.CharField(max_length=40, blank=False)
	description = models.CharField(max_length=100, blank=False)
	cost = models.DecimalField(decimal_places=2, max_digits=7, blank=False)
	
	def __str__(self):
		return self.name