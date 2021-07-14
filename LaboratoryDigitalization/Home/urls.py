from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("firstyear", views.firstyear, name='firstyear'),
    path("inft", views.inft, name='inft'),
    path("cmpn", views.cmpn, name='cmpn'),
    path("extc", views.extc, name='extc'),
    path("etrx", views.etrx, name='etrx'),
    path("biomed", views.biomed, name='biomed'),


]