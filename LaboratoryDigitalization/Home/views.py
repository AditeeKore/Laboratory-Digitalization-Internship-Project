from django.contrib.messages.api import warning
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from django import forms
from .models import AllLabinfo, Lab7A, Lab7B, Lab7C, Lab7D, Lab7E, Lab7A_SW_Inst, Lab7B_SW_Inst, Lab7C_SW_Inst, Lab7D_SW_Inst, Lab7E_SW_Inst
from .resources import uploadresource
from django.contrib import messages
from tablib import Dataset
from .models import Lab7A
# Create your views here.

def lab7Ainfo(request):
    lab7a_pc_list = Lab7A.objects.all()
    return render(request, 'inft.html', {'lab7a_pc_list': lab7a_pc_list})

def labBinfo(request):
    lab7b_pc_list = Lab7B.objects.all()
    return render(request, 'inft.html', {'lab7b_pc_list': lab7b_pc_list})


def upload(request):
    if request.method == "POST":
        upload_resource = uploadresource()
        dataset = Dataset()
        new_lab= request.FILES['myfile']

        if not new_lab.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_lab.read(),format='xlsx')
        for data in imported_data:
            value = upload(
                data[0],
                # data[1],
                # data[2],
                # data[3],
                # data[4],
            )
            value.save()
    return render(request, 'upload.html')



    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         request.FILES['file'].save_to_database(
    #             model=upload,
    #             mapdict=['Lab', 'NumberofPCs', 'BasicConfig', 'PCspurchasedinYr', 'OS', 'SpecialSoftware'])
    #         return HttpResponse("OK")
    #     else:
    #         return HttpResponseBadRequest()
    # else:
    #     return render(request, 'upload.html', {})



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def firstyear(request):
    return render(request, 'firstyear.html')

def inft(request):
    return render(request, 'inft.html')
# def inftse(request):
#     return render(request, 'inftse.html')
# def inftte(request):
#     return render(request, 'inftte.html')
# def inftbe(request):
#     return render(request, 'inftbe.html')

def cmpn(request):
    return render(request, 'cmpn.html')
# def cmpnse(request):
#     return render(request, 'cmpnse.html')
# def cmpnte(request):
#     return render(request, 'cmpnte.html')
# def cmpnbe(request):
#     return render(request, 'cmpnbe.html')

def extc(request):
    return render(request, 'extc.html')
# def extcse(request):
#     return render(request, 'extcse.html')
# def extcte(request):
#     return render(request, 'extcte.html')
# def extcbe(request):
#     return render(request, 'extcbe.html')

def etrx(request):
    return render(request, 'etrx.html')
# def etrxse(request):
#     return render(request, 'etrxse.html')
# def etrxte(request):
#     return render(request, 'etrxte.html')
# def etrxbe(request):
#     return render(request, 'etrxbe.html')

def biomed(request):
    return render(request, 'biomed.html')
# def biomedse(request):
#     return render(request, 'biomedse.html')
# def biomedte(request):
#     return render(request, 'biomedte.html')
# def biomedbe(request):
#     return render(request, 'biomedbe.html')

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

class UploadFileForm(forms.Form):
    file = forms.FileField()

