from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def firstyear(request):
    return render(request, 'firstyear.html')

def inft(request):
    return render(request, 'inft.html')

def cmpn(request):
    return render(request, 'cmpn.html')

def extc(request):
    return render(request, 'extc.html')

def etrx(request):
    return render(request, 'etrx.html')

def biomed(request):
    return render(request, 'biomeds.html')



