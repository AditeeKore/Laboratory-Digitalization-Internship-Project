from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("firstyear", views.firstyear, name='firstyear'),
    path("inft", views.inft, name='inft'),
    # path("inftse", views.inftse, name='inftse'),
    # path("inftte", views.inftte, name='inftte'),
    # path("inftbe", views.inftbe, name='inftbe'),
    path("cmpn", views.cmpn, name='cmpn'),
    # path("cmpnse", views.cmpnse, name='cmpnse'),
    # path("cmpnte", views.cmpnte, name='cmpnte'),
    # path("cmpnbe", views.cmpnbe, name='cmpnbe'),
    path("extc", views.extc, name='extc'),
    # path("extcse", views.extcse, name='extcse'),
    # path("extcte", views.extcte, name='extcte'),
    # path("extcbe", views.extcbe, name='extcbe'),
    path("etrx", views.etrx, name='etrx'),
    # path("etrxse", views.etrxse, name='etrxse'),
    # path("etrxte", views.etrxte, name='etrxte'),
    # path("etrxbe", views.etrxbe, name='etrxbe'),
    path("biomed", views.biomed, name='biomed'),
    # path("biomedse", views.biomedse, name='biomedse'),
    # path("biomedte", views.biomedte, name='biomedte'),
    # path("biomedbe", views.biomedbe, name='biomedbe'),
    path("bee", views.bee, name='bee'),
    path("chemistry", views.chemistry, name='chemistry'),
    path("cprog", views.cprog, name='cprog'),
    path("engdrawing", views.engdrawing, name='engdrawing'),
    path("math1", views.math1, name='math1'),
    path("mechanics", views.mechanics, name='mechanics'),
    path("miniproject1", views.miniproject1, name='miniproject1'),
    path("physics", views.physics, name='physics'),
    path("Upload", views.upload, name='upload'),


    


    



]