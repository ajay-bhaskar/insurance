from django import forms
from .models import insuranceData

class updateForm(forms.ModelForm):
    class Meta:
        model=insuranceData
        fields="__all__"
        