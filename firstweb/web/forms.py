from django import forms
from .models import Web
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WebForm(forms.ModelForm):
    
    class Meta:
        model = Web
        fields = ["text","photo"]


class UserRagistrationform(UserCreationForm):
    Email=forms.EmailField()
    class meta:
        model=User
        fields=('username', 'eamil', 'password1','password2')

