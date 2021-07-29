from django import forms
from django.forms import ModelForm

from .models import Trainee

class DateInput(forms.DateInput):
    input_type = 'date'

class TraineeForm(ModelForm):
    class Meta:
        model =  Trainee
        fields = '__all__'
        widgets = {
            'DOB': DateInput(),
            'date_of_Program':DateInput(),
        }