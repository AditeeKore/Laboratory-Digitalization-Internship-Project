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

# def labBinfo(request):
#     lab7b_pc_list = Lab7B.objects.all()
#     return render(request, 'lab7a.html', {'lab7b_pc_list': lab7b_pc_list})

def lab7aswinfo(request):
    lab7aswinfo_list = Lab7A_SW_Inst.objects.all()
    return render(request, 'lab7aswinfo.html', {'lab7aswinfo_list': lab7aswinfo_list})

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

def lab7aswinfo(request):
    return render(request, 'lab7aswinfo.html')

def lab7a(request):
    return render(request, 'lab7a.html')


class UploadFileForm(forms.Form):
    file = forms.FileField()

