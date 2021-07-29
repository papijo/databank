from django import forms
from django.forms import ModelForm, widgets

from .models import StaffBio

class DateInput(forms.DateInput):
    input_type = 'date'

class StaffBioForm(ModelForm):
    
    class Meta:
        model = StaffBio
        fields = '__all__'
        widgets = {
            'DOB': DateInput(),
            'DOE': DateInput(),
            'leave_Start': DateInput(),
            'leave_End': DateInput(),
        }
