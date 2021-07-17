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

def bee(request):
    return render(request, 'bee.html')

def chemistry(request):
    return render(request, 'chemistry.html')

def cprog(request):
    return render(request, 'cprog.html')

def engdrawing(request):
    return render(request, 'engdrawing.html')

def math1(request):
    return render(request, 'math1.html')

def mechanics(request):
    return render(request, 'mechanics.html')

def miniproject1(request):
    return render(request, 'miniproject1.html')

def physics(request):
    return render(request, 'physics.html')



