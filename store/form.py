from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widget = {'name': TextInput(attrs={'class': 'form-control'}),
                  'email':EmailInput(attrs={'class': 'form-control'})
                  }

'''
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nom',
        max_length= 100,
        widget=forms.TextInput(attrs={'class':'forms-control'}),
        required=True
    )
    email = forms.CharField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'forms-control'}),
        required=True

    )
'''