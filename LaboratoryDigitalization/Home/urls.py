from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("firstyear", views.firstyear, name='firstyear'),
    path("inft", views.lab7Ainfo, name='inft'),
    path("Upload", views.upload, name='upload'),


    


    



]