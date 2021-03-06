"""basicSite URL Configuration
	The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basicapp/', include('basicApp.urls')),
]
