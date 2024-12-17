from django import forms
from .models import *

class loginForm(forms.Form):
    username = forms.CharField(max_length= 20, required=True, label='Username')
    pass1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label='Password')
    
