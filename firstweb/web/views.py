from django.shortcuts import render
from .models import Web
from .forms import WebForm
from django.shortcuts import get_object_or_404,redirect

def index(request):
    return render (request, 'index.html')
# Create your views here.
def weeb_list(request):
    Web.objects.all().order_by("-created_at")
    return render(request, 'web_list.html',{'web':Web})

def web_created(request):
    if request.method == 'POST': 
        form = WebForm(request.POST,request.FILES)
        if form.is_valid():
            web=form.save(commit= False)
            web.user()= request.user()
            web.save()
            return redirect('web_list')
    else:
        form =WebForm()
    return render(request, 'web_from.html',{'from':form})

def web_edit(request):
    web=None
    if :
        pass
    else:
        form= WebForm(instance= web)
