from django.contrib.messages.api import warning
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseBadRequest
from django import forms
from .models import AllLabinfo, Lab7A, Lab7B, Lab7C, Lab7D, Lab7E, Lab7A_SW_Inst, Lab7B_SW_Inst, Lab7C_SW_Inst, Lab7D_SW_Inst, Lab7E_SW_Inst, tt_file, lab_ready_cert
from .resources import uploadresource
from django.contrib import messages
from tablib import Dataset
from .models import Lab7A
from .forms import tt_file_form, lab_ready_cert_form
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/index')

def lab7Ainfo(request):
    lab7a_pc_list = Lab7A.objects.all()
    return render(request, 'lab7acompinfo.html', {'lab7a_pc_list': lab7a_pc_list})

def lab7A(request):
    return render(request, 'lab7a.html')

def lab7B(request):
    return render(request, 'lab7b.html')

def lab7C(request):
    return render(request, 'lab7c.html')

def lab7D(request):
    return render(request, 'lab7d.html')

def lab7E(request):
    return render(request, 'lab7e.html')


def lab7Binfo(request):
    lab7b_pc_list = Lab7B.objects.all()
    return render(request, 'lab7bcompinfo.html', {'lab7b_pc_list': lab7b_pc_list})

def lab7Cinfo(request):
    lab7c_pc_list = Lab7C.objects.all()
    return render(request, 'lab7ccompinfo.html', {'lab7c_pc_list': lab7c_pc_list})

def lab7Dinfo(request):
    lab7d_pc_list = Lab7D.objects.all()
    return render(request, 'lab7dcompinfo.html', {'lab7d_pc_list': lab7d_pc_list})

def lab7Einfo(request):
    lab7e_pc_list = Lab7E.objects.all()
    return render(request, 'lab7ecompinfo.html', {'lab7e_pc_list': lab7e_pc_list})

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

@login_required(login_url='/admin/login/?next=/admin/')
@staff_member_required
def upload(request):
    if request.method == "POST":
        form = tt_file_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New file uploaded')
    else:
        form = tt_file_form()
    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/admin/login/?next=/admin/')
@staff_member_required
def cert_upload(request):            
    if request.method == "POST":
        form = lab_ready_cert_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Certificate file uploaded')
    else:
        form = lab_ready_cert_form()
    return render(request, 'cert_upload.html', {'form': form})

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

def timetable(request):
    timetable_file = tt_file.objects.all()
    return render(request, 'timetable.html', {'timetable_file': timetable_file})

def lab_cert(request):
    cert_file = lab_ready_cert.objects.all()
    return render(request, 'lab_cert.html', {'cert_file': cert_file})  

class UploadFileForm(forms.Form):
    file = forms.FileField()

