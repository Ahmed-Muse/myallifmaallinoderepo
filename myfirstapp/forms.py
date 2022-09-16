from unicodedata import name
from django import forms
from .models import *
class NamesForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = namesmodel
        fields = ["name","myimage","mydocument"]