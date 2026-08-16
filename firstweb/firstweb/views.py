from django.shortcuts import render

def webpage(request):
    return render(request, 'web_list.html')