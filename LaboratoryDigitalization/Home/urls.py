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
    path("bee", views.bee, name='bee'),
    path("chemistry", views.chemistry, name='chemistry'),
    path("cprog", views.cprog, name='cprog'),
    path("engdrawing", views.engdrawing, name='engdrawing'),
    path("math1", views.math1, name='math1'),
    path("mechanics", views.mechanics, name='mechanics'),
    path("miniproject1", views.miniproject1, name='miniproject1'),
    path("physics", views.physics, name='physics'),

    


    



]