from django.shortcuts import render
from .models import Web
from .forms import WebForm

def index(request):
    return render (request, 'index.html')
# Create your views here.
