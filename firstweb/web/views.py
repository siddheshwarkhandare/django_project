from django.shortcuts import render
from .models import Web
from .forms import WebForm
from django.shortcuts import get_object_or_404

def index(request):
    return render (request, 'index.html')
# Create your views here.
def weeb_list(request):
    Web.objects.all().order_by("-created_at")
    return render(request, 'web_list.html',{'web':Web})

def web_created(request):
    if request.method == 'POST': 
        pass
    else:
        form =WebForm()
    return render(request, 'webfrom_list.html',{'from':form})
