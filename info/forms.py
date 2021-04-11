from django import forms
from django.forms import ModelForm
from .models import Found

#create a form
class FoundForm(ModelForm):
    class Meta:
        model = Found
        fields = ('location', 'city', 'name', 'phone', 'photo',)

        labels = {
            'location':'' ,
            'city': '',
            'name': '',
            'phone': '',
            'photo': '',
        
        }

        widgets = {
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'photo': forms.FileInput(attrs={'class':'form-label',}),
        }

