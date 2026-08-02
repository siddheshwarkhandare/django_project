from django.shortcuts import render
from .models import Web
from .forms import WebForm
from django.shortcuts import get_object_or_404

def index(request):
    return render (request, 'index.html')
# Create your views here.
