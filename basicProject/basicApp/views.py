from django.shortcuts import render
from django.http import HttpResponse
from basicApp.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the basicApp index. hi monica!!!")

def home(request):
    return render(request, 'home.html')

def books(request):
	booksQuerySet = Book.objects.all()
	return render(request, 'books.html', {'booksQS': booksQuerySet})

def products(request):
	productsQuerySet = Product.objects.all()
	return render(request, 'products.html', {'productsQS': productsQuerySet})

