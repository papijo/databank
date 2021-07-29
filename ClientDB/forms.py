from django import forms
from django.forms import ModelForm, widgets 

from .models import ClientOrganisation

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientOrganisationForm(ModelForm):
    class Meta:
        model =  ClientOrganisation
        fields = '__all__'
        widgets = {
            'date_formed': DateInput(),
        }