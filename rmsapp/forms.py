from django import forms
from rmsapp.models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        exclude = ('otp',)