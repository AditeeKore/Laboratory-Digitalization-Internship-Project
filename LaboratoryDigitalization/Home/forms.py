from django import forms
from django.forms import fields
from .models import tt_file, lab_ready_cert

class tt_file_form(forms.ModelForm):
    class Meta:
        model = tt_file
        fields = {'lab_no', 'tt_pdf'}

class lab_ready_cert_form(forms.ModelForm):
    class Meta:
        model = lab_ready_cert
        fields = {'lab_no', 'cert_pdf'}