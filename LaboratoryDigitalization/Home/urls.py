from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("logout", views.logout, name='logout'),
    path("userlogin", views.userlogin, name='userlogin'),

    #LAB 7
    path("lab7", views.lab7, name='lab7'),
    path("lab7a", views.lab7A, name='lab7a'),
    path("lab7b", views.lab7B, name='lab7b'),
    path("lab7c", views.lab7C, name='lab7c'),
    path("lab7d", views.lab7D, name='lab7d'),
    path("lab7e", views.lab7E, name='lab7e'),
    path("lab7acompinfo", views.lab7Ainfo, name='lab7acompinfo'),
    path("lab7bcompinfo", views.lab7Binfo, name='lab7bcompinfo'),
    path("lab7ccompinfo", views.lab7Cinfo, name='lab7ccompinfo'),
    path("lab7dcompinfo", views.lab7Dinfo, name='lab7dcompinfo'),
    path("lab7ecompinfo", views.lab7Einfo, name='lab7ecompinfo'),
    path('lab7aswinfo', views.lab7aswinfo, name='lab7aswinfo'),
    path('lab7bswinfo', views.lab7bswinfo, name='lab7bswinfo'),
    path('lab7cswinfo', views.lab7cswinfo, name='lab7cswinfo'),
    path('lab7dswinfo', views.lab7dswinfo, name='lab7dswinfo'),
    path('lab7eswinfo', views.lab7eswinfo, name='lab7eswinfo'),

    #LAB CC
    path("labcc", views.labcc, name='labcc'),
    path("labcc1", views.labcc1, name='labcc1'),
    path("labcc2", views.labcc2, name='labcc2'),
    path("labcc3", views.labcc3, name='labcc3'),
    path("labcc1compinfo.html", views.labcc1compinfo, name='labcc1compinfo'),
    path("labcc2compinfo.html", views.labcc2compinfo, name='labcc2compinfo'),
    path("labcc3compinfo.html", views.labcc3compinfo, name='labcc3compinfo'),
    path("labcc1swinfo", views.labcc1swinfo, name='labcc1swinfo'),
    path("labcc2swinfo", views.labcc2swinfo, name='labcc2swinfo'),
    path("labcc3swinfo", views.labcc3swinfo, name='labcc3swinfo'),

    #LAB 5
    path("lab5", views.lab5, name='lab5'),
    path("lab5a", views.lab5a, name='lab5a'),
    path("lab5b", views.lab5b, name='lab5b'),
    path("lab5c", views.lab5c, name='lab5c'),
    path("lab5d", views.lab5d, name='lab5d'),
    path("lab5e", views.lab5e, name='lab5e'),
    path("lab5acompinfo", views.lab5acompinfo, name='lab5acompinfo'),
    path("lab5bcompinfo", views.lab5bcompinfo, name='lab5bcompinfo'),
    path("lab5ccompinfo", views.lab5ccompinfo, name='lab5ccompinfo'),
    path("lab5dcompinfo", views.lab5dcompinfo, name='lab5dcompinfo'),
    path("lab5ecompinfo", views.lab5ecompinfo, name='lab5ecompinfo'),
    path("lab5aswinfo", views.lab5aswinfo, name='lab5aswinfo'),
    path("lab5bswinfo", views.lab5bswinfo, name='lab5bswinfo'),
    path("lab5cswinfo", views.lab5cswinfo, name='lab5cswinfo'),
    path("lab5dswinfo", views.lab5dswinfo, name='lab5dswinfo'),
    path("lab5eswinfo", views.lab5eswinfo, name='lab5eswinfo'),

    #LAB 11
    path("lab11", views.lab11, name='lab11'),
    path("lab11a", views.lab11a, name='lab11a'),
    path("lab11b", views.lab11b, name='lab11b'),
    path("lab11acompinfo", views.lab11acompinfo, name='lab11acompinfo'),
    path("lab11bcompinfo", views.lab11bcompinfo, name='lab11bcompinfo'),
    path("lab11aswinfo", views.lab11aswinfo, name='lab11aswinfo'),
    path("lab11bswinfo", views.lab11bswinfo, name='lab11bswinfo'),
    

    path("upload", views.upload, name='upload'),
    path("cert_upload", views.cert_upload, name='cert_upload'),
    path("lab_cert", views.lab_cert, name='lab_cert'),
    path("timetable", views.timetable, name='timetable'),
    

]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

