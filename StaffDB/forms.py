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
            'date_of_Birth': DateInput(),
            'date_of_Employment': DateInput(),
            'leave_Start': DateInput(),
            'leave_End': DateInput(),
            'date_of_Last_Promotion': DateInput(),
            'date_of_next_Promotion': DateInput(),
        }
