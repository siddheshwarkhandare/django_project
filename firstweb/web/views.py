from django.shortcuts import render
from .models import Web
from .forms import WebForm
from django.shortcuts import get_object_or_404,redirect

"""
in views we define the fuctionality of forms we creat each function for the for form 
after this we are loading this views in to the jija template

"""
#in this function we are defining the form 
def index(request):
    return render (request, 'index.html')# rending the form
# Create your views here.
def web_list(request):
    Web.objects.all().order_by("-created_at") # listing all the form in page 
    return render(request, 'web_list.html',{'web':Web})  # listing all the web in to this web page 
                                                        #"web is passing the data from web that is modle file"
# in this fuction we are creating an new entry like tweet 
def web_created(request):
    if request.method == 'POST': 
        form = WebForm(request.POST,request.FILES) # importing from from the model file 
                                                    #django creat an form by self and we can use that form 
        if form.is_valid():# if the data is valid than we can save that form in db
            web=form.save(commit= False)#just saving the form not saving it
            web.user()= request.user() #geting the user form request 
            web.save()#saving the form 
            return redirect('web_list')#all the if satement is post
    else:
        form =WebForm()
    return render(request, 'web_form.html',{'from':form}) #we will seeing the form because of this

def web_edit(request,web_id):
    web= get_object_or_404(Web,pk=web_id,user=request.user)
    if request.method == 'POST':
        form = WebForm(request.POST,request.FILES,instance=web)
        if form.is_valid():
            web.user.save(commit=False)
            web.user() = request.user()
            web.save
            return redirect('web_list')
    else:
        form= WebForm(instance= web)# keeping the data prefill
    return render(request,'web_form.html', {'form':form})

def web_delete(request, web_id):
    web=get_object_or_404(Web,pk=web_id, user=request.user)
    if request.method == 'POST':
        web.delete()
        return redirect('web_list')
    return render(request,'web_conf_delete.html', {'web':web})
