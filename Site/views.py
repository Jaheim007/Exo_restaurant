from django.shortcuts import render

def home(request): 
    return render(request, 'display\index.html')

# Create your views here.
