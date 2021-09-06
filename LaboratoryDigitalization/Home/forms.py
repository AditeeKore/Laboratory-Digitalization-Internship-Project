from django import forms
from django.forms import fields
from .models import tt_file

class tt_file_form(forms.ModelForm):
    class Meta:
        model = tt_file
        fields = {'lab_no', 'tt_pdf'}