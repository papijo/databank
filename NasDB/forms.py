from django.db.models import fields
from django import forms
from django.forms import ModelForm, widgets 

from .models import NasOrganisation, InstructionalStaff

class DateInput(forms.DateInput):
    input_type = 'date'

class NasOrganisationForm(ModelForm):
    class Meta:
        model =  NasOrganisation
        fields = '__all__'
        widgets = {
            'YOE': DateInput(),
            'DOPA':DateInput(),
            'DOFA': DateInput(),
        }

class InstructionalStaffForm(ModelForm):
    class Meta:
        model = InstructionalStaff
        fields = '__all__'
        widgets = {
            'doe': DateInput()
        }