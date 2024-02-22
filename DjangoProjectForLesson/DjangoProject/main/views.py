from django.shortcuts import render
from .models import *
# Create your views here.
def page(request):
    article = list(Python.objects.all())
    return render(request, 'main/index.html' , {'article': article})

def page2(request):
    article = list(JavaScript.objects.all())
    return render(request, 'main/index.html' , {'article': article})
