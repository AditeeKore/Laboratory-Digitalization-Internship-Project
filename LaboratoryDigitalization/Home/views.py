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
    return render(request, 'lab7a.html', {'lab7a_pc_list': lab7a_pc_list})

def lab7Binfo(request):
    lab7b_pc_list = Lab7B.objects.all()
    return render(request, 'lab7b.html', {'lab7b_pc_list': lab7b_pc_list})

def lab7Cinfo(request):
    lab7c_pc_list = Lab7C.objects.all()
    return render(request, 'lab7c.html', {'lab7c_pc_list': lab7c_pc_list})

def lab7Dinfo(request):
    lab7d_pc_list = Lab7D.objects.all()
    return render(request, 'lab7d.html', {'lab7d_pc_list': lab7d_pc_list})

def lab7Einfo(request):
    lab7e_pc_list = Lab7E.objects.all()
    return render(request, 'lab7e.html', {'lab7e_pc_list': lab7e_pc_list})

def lab7aswinfo(request):
    lab7ainfo_list = Lab7A_SW_Inst.objects.all()
    return render(request, 'lab7aswinfo.html', {'lab7ainfo_list': lab7ainfo_list})

def lab7bswinfo(request):
    lab7binfo_list = Lab7B_SW_Inst.objects.all()
    return render(request, 'lab7bswinfo.html', {'lab7binfo_list': lab7binfo_list})

def lab7cswinfo(request):
    lab7cinfo_list = Lab7C_SW_Inst.objects.all()
    return render(request, 'lab7cswinfo.html', {'lab7cinfo_list': lab7cinfo_list})

def lab7dswinfo(request):
    lab7dinfo_list = Lab7D_SW_Inst.objects.all()
    return render(request, 'lab7dswinfo.html', {'lab7dinfo_list': lab7dinfo_list})

def lab7eswinfo(request):
    lab7einfo_list = Lab7E_SW_Inst.objects.all()
    return render(request, 'lab7eswinfo.html', {'lab7einfo_list': lab7einfo_list})


# def upload(request):
#     if request.method == "POST":
        # upload_file = 
        



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

def lab7aswinfo(request):
    return render(request, 'lab7aswinfo.html')

def lab7bswinfo(request):
    return render(request, 'lab7bswinfo.html')

def lab7a(request):
    return render(request, 'lab7a.html')

def lab7b(request):
    return render(request, 'lab7b.html')

def lab7(request):
    return render(request, 'lab7.html')

class UploadFileForm(forms.Form):
    file = forms.FileField()

