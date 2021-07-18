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
def inftse(request):
    return render(request, 'inftse.html')
def inftte(request):
    return render(request, 'inftte.html')
def inftbe(request):
    return render(request, 'inftbe.html')

def cmpn(request):
    return render(request, 'cmpn.html')
def cmpnse(request):
    return render(request, 'cmpnse.html')
def cmpnte(request):
    return render(request, 'cmpnte.html')
def cmpnbe(request):
    return render(request, 'cmpnbe.html')

def extc(request):
    return render(request, 'extc.html')
def extcse(request):
    return render(request, 'extcse.html')
def extcte(request):
    return render(request, 'extcte.html')
def extcbe(request):
    return render(request, 'extcbe.html')

def etrx(request):
    return render(request, 'etrx.html')
def etrxse(request):
    return render(request, 'etrxse.html')
def etrxte(request):
    return render(request, 'etrxte.html')
def etrxbe(request):
    return render(request, 'etrxbe.html')

def biomed(request):
    return render(request, 'biomed.html')
def biomedse(request):
    return render(request, 'biomedse.html')
def biomedte(request):
    return render(request, 'biomedte.html')
def biomedbe(request):
    return render(request, 'biomedbe.html')

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



