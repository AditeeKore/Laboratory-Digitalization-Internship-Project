from Home.availability import availibility
from django.contrib.messages.api import warning
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseBadRequest
from django import forms
from .models import *
from .resources import uploadresource
from django.contrib import messages
from tablib import Dataset
from .models import Lab7A
from .forms import tt_file_form, lab_ready_cert_form
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!!")
                return redirect('/index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()          
    return render(request, 'userlogin.html', {"login_form":form})

def logout(request):
    auth.logout(request)
    return redirect('/index')

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

def lab7(request):
    return render(request, 'lab7.html')

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

def lab7Ainfo(request):
    lab7a_pc_list = Lab7A.objects.all()
    return render(request, 'lab7acompinfo.html', {'lab7a_pc_list': lab7a_pc_list})

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

def lab7aswinfo(request):
    return render(request, 'lab7aswinfo.html')

def lab7bswinfo(request):
    return render(request, 'lab7bswinfo.html')

# def lab7a(request):
#     return render(request, 'lab7a.html')

# def lab7b(request):
#     return render(request, 'lab7b.html')

# LAB CC
def labcc(request):
    return render(request, 'labcc.html')

def labcc1(request):
    return render(request, 'labcc1.html')

def labcc2(request):
    return render(request, 'labcc2.html')

def labcc3(request):
    return render(request, 'labcc3.html') 

def labcc1compinfo(request):
    labcc1_pc_list = LabCC1.objects.all()
    return render(request, 'labcc1compinfo.html', {'labcc1_pc_list': labcc1_pc_list})

def labcc2compinfo(request):
    labcc2_pc_list = LabCC2.objects.all()
    return render(request, 'labcc2compinfo.html', {'labcc2_pc_list': labcc2_pc_list})

def labcc3compinfo(request):
    labcc3_pc_list = LabCC3.objects.all()
    return render(request, 'labcc3compinfo.html', {'labcc3_pc_list': labcc3_pc_list})

def labcc1swinfo(request):
    labcc1info_list = LabCC1_SW_Inst.objects.all()
    return render(request, 'labcc1swinfo.html', {'labcc1info_list': labcc1info_list})

def labcc2swinfo(request):
    labcc2info_list = LabCC2_SW_Inst.objects.all()
    return render(request, 'labcc2swinfo.html', {'labcc2info_list': labcc2info_list})

def labcc3swinfo(request):
    labcc3info_list = LabCC3_SW_Inst.objects.all()
    return render(request, 'labcc3swinfo.html', {'labcc3info_list': labcc3info_list})

#LAB 5
def lab5(request):
    return render(request, 'lab5.html')

def lab5a(request):
    return render(request, 'lab5a.html')

def lab5b(request):
    return render(request, 'lab5b.html')

def lab5c(request):
    return render(request, 'lab5c.html')

def lab5d(request):
    return render(request, 'lab5d.html')

def lab5e(request):
    return render(request, 'lab5e.html')

def lab5acompinfo(request):
    lab5a_pc_list = Lab5A.objects.all()
    return render(request, 'lab5acompinfo.html', {'lab5a_pc_list': lab5a_pc_list})

def lab5bcompinfo(request):
    lab5b_pc_list = Lab5B.objects.all()
    return render(request, 'lab5bcompinfo.html', {'lab5b_pc_list': lab5b_pc_list})

def lab5ccompinfo(request):
    lab5c_pc_list = Lab5C.objects.all()
    return render(request, 'lab5ccompinfo.html', {'lab5c_pc_list': lab5c_pc_list})

def lab5dcompinfo(request):
    lab5d_pc_list = Lab5D.objects.all()
    return render(request, 'lab5dcompinfo.html', {'lab5d_pc_list': lab5d_pc_list})

def lab5ecompinfo(request):
    lab5e_pc_list = Lab5E.objects.all()
    return render(request, 'lab5ecompinfo.html', {'lab5e_pc_list': lab5e_pc_list})

def lab5aswinfo(request):
    lab5ainfo_list = Lab5A_SW_Inst.objects.all()
    return render(request, 'lab5aswinfo.html', {'lab5ainfo_list': lab5ainfo_list})

def lab5bswinfo(request):
    lab5binfo_list = Lab5B_SW_Inst.objects.all()
    return render(request, 'lab5bswinfo.html', {'lab5binfo_list': lab5binfo_list})

def lab5cswinfo(request):
    lab5cinfo_list = Lab5C_SW_Inst.objects.all()
    return render(request, 'lab5cswinfo.html', {'lab5cinfo_list': lab5cinfo_list})

def lab5dswinfo(request):
    lab5dinfo_list = Lab5D_SW_Inst.objects.all()
    return render(request, 'lab5dswinfo.html', {'lab5dinfo_list': lab5dinfo_list})

def lab5eswinfo(request):
    lab5einfo_list = Lab5E_SW_Inst.objects.all()
    return render(request, 'lab5swinfoe.html', {'lab5einfo_list': lab5einfo_list})

#LAB 11
def lab11(request):
    return render(request, 'lab11.html')  

def lab11a(request):
    return render(request, 'lab11a.html') 

def lab11b(request):
    return render(request, 'lab11b.html') 

def lab11aswinfo(request):
    lab11ainfo_list = Lab11A_SW_Inst.objects.all()
    return render(request, 'lab11aswinfo.html', {'lab11ainfo_list': lab11ainfo_list}) 

def lab11bswinfo(request):
    lab11binfo_list = Lab11B_SW_Inst.objects.all()
    return render(request, 'lab11bswinfo.html', {'lab11binfo_list': lab11binfo_list}) 

def lab11acompinfo(request):
    lab11a_pc_list = Lab11A.objects.all()
    return render(request, 'lab11acompinfo.html', {'lab11a_pc_list': lab11a_pc_list}) 

def lab11bcompinfo(request):
    lab11b_pc_list = Lab11B.objects.all()
    return render(request, 'lab11bcompinfo.html', {'lab11b_pc_list': lab11b_pc_list}) 

def timetable(request):
    timetable_file = tt_file.objects.all().order_by('lab_no')
    return render(request, 'timetable.html', {'timetable_file': timetable_file})

def lab_cert(request):
    cert_file = lab_ready_cert.objects.all().order_by('lab_no')
    return render(request, 'lab_cert.html', {'cert_file': cert_file})  

class UploadFileForm(forms.Form):
    file = forms.FileField()



def booking(request):
    dropdown=User.objects.all()
    dropdown_2=Booking_Labs.objects.all()
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        lab_no = request.POST.get('lab_no')
        slot_time = request.POST.get('slot_time')
        slot_date = request.POST.get('slot_date')
        booked_by = request.POST.get('booked_by')
        booking = Slot_Booking(event_name=event_name, lab_no=lab_no, slot_time=slot_time, slot_date=slot_date, booked_by=booked_by)
        if availibility(lab_no, slot_date, slot_time ):
            messages.warning(request, 'This slot is already booked, please book another slot')
            return redirect('/booking')

        booking.save()
        messages.success(request, 'Your slot is saved')
        return redirect('/index')
    return render(request, 'booking.html', {'User': dropdown, 'Booking_Labs': dropdown_2})

def display_slot(request):
    lab_booking = Slot_Booking.objects.all().order_by('lab_no')
    return render(request, 'display_slot.html', {'lab_booking': lab_booking})

def lab5_tt(request):
    lab5a_tt_list = Lab5A_tt_booking.objects.all()
    lab5b_tt_list = Lab5B_tt_booking.objects.all()
    lab5c_tt_list = Lab5C_tt_booking.objects.all()
    lab5d_tt_list = Lab5D_tt_booking.objects.all()
    lab5e_tt_list = Lab5E_tt_booking.objects.all()
    return render(request, 'lab5_tt.html', {'lab5a_tt_list':lab5a_tt_list, 'lab5b_tt_list':lab5b_tt_list, 'lab5c_tt_list':lab5c_tt_list, 'lab5d_tt_list':lab5d_tt_list, 'lab5e_tt_list':lab5e_tt_list})

def lab7_tt(request):
    lab7a_tt_list = Lab7A_tt_booking.objects.all()
    lab7b_tt_list = Lab7B_tt_booking.objects.all()
    lab7c_tt_list = Lab7C_tt_booking.objects.all()
    lab7d_tt_list = Lab7D_tt_booking.objects.all()
    lab7e_tt_list = Lab7E_tt_booking.objects.all()
    return render(request, 'lab7_tt.html', {'lab7a_tt_list':lab7a_tt_list, 'lab7b_tt_list':lab7b_tt_list, 'lab7c_tt_list':lab7c_tt_list, 'lab7d_tt_list':lab7d_tt_list, 'lab7e_tt_list':lab7e_tt_list})

def lab11_tt(request):
    lab11a_tt_list = Lab11A_tt_booking.objects.all()
    lab11b_tt_list = Lab11B_tt_booking.objects.all()
    return render(request, 'lab11_tt.html', {'lab11a_tt_list':lab11a_tt_list, 'lab11b_tt_list':lab11b_tt_list})

def labcc_tt(request):
    labcc1_tt_list = LabCC1_tt_booking.objects.all()
    labcc2_tt_list = LabCC2_tt_booking.objects.all()
    labcc3_tt_list = LabCC3_tt_booking.objects.all()
    return render(request, 'labcc_tt.html', {'labcc1_tt_list':labcc1_tt_list, 'labcc2_tt_list':labcc2_tt_list, 'labcc3_tt_list':labcc3_tt_list})




    