from .models import *
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse



def availibility(lab_no, slot_date, slot_time):
        avail_list=False
        booking_list = Slot_Booking.objects.filter(lab_no=lab_no,slot_date=slot_date, slot_time=slot_time)
        for booking in booking_list:
            if booking.lab_no == lab_no and booking.slot_date == slot_date and booking.slot_time == slot_time:
                avail_list=False
            else:
                avail_list=True
        return avail_list