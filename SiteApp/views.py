from django.shortcuts import render

from . import models

def home(request): 
    banner = models.Banner.objects.filter(status=True).first()
    return render(request, 'display/index.html', locals())

# Create your views here.
