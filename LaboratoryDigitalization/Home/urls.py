from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("lab7", views.lab7, name='lab7'),
    path("lab7a", views.lab7Ainfo, name='lab7a'),
    path("lab7b", views.lab7Binfo, name='lab7b'),
    path("lab7c", views.lab7Cinfo, name='lab7c'),
    path("lab7d", views.lab7Dinfo, name='lab7d'),
    path("lab7e", views.lab7Einfo, name='lab7e'),
    path("upload", views.upload, name='upload'),
    path("cert_upload", views.cert_upload, name='cert_upload'),
    path("lab_ready_cert", views.lab_ready_cert, name='lab_ready_cert'),
    path("timetable", views.timetable, name='timetable'),
    path('lab7aswinfo', views.lab7aswinfo, name='lab7aswinfo'),
    path('lab7bswinfo', views.lab7bswinfo, name='lab7bswinfo'),
    path('lab7cswinfo', views.lab7cswinfo, name='lab7cswinfo'),
    path('lab7dswinfo', views.lab7dswinfo, name='lab7dswinfo'),
    path('lab7eswinfo', views.lab7eswinfo, name='lab7eswinfo'),

]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

