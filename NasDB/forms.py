from django import forms
from django.forms import ModelForm, widgets 

from .models import NasOrganisation

class DateInput(forms.DateInput):
    input_type = 'date'

class NasOrganisationForm(ModelForm):
    class Meta:
        model =  NasOrganisation
        fields = '__all__'
        widgets = {
            'YOE': DateInput(),
            'DOPA':DateInput(),
        }