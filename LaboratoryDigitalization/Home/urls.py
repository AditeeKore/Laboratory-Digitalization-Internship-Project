from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("lab7", views.lab7, name='lab7'),
    path("lab7a", views.lab7Ainfo, name='lab7a'),
    path("lab7b", views.lab7Binfo, name='lab7b'),
    path("Upload", views.upload, name='upload'),
    path('lab7aswinfo', views.lab7aswinfo, name='lab7aswinfo'),
    path('lab7bswinfo', views.lab7bswinfo, name='lab7bswinfo'),
    

    


    



]