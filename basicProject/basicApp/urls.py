"""basicApp URL Configuration
	The `urlpatterns` list app routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('products/', views.products, name='productz'),
]