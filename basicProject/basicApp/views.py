from django.shortcuts import render
from django.http import HttpResponse
from basicApp.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the basicApp index.")

def home(request):
    return render(request, 'home.html')

def books(request):
	booksQuerySet = Book.objects.all()
	return render(request, 'books.html', {'booksQS': booksQuerySet})

