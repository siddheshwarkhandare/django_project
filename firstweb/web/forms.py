from django import forms
from .models import Web


class WebForm(forms.ModelForm):
    
    class Meta:
        model = Web
        fields = ("text","photo")
