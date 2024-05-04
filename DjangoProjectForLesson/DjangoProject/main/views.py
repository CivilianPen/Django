from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
# Create your views here.

def main(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Reviews.objects.create(**form.cleaned_data)
                return  redirect('main')
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostForm()
        review = list(Reviews.objects.all())
    return render(request, 'main/main.html' , {'form': form ,'review' : review})
def page(request):
    article = list(Python.objects.all())
    return render(request, 'main/index.html' , {'article': article})

def page2(request):
    article = list(JavaScript.objects.all())
    return render(request, 'main/index2.html' , {'article': article})

def PostF(request,post_id):
    article = list(Python.objects.filter(pk=post_id))
    return render(request, "Full.html", {"article": article})

def PostF2(request,post_id):
    article = list(JavaScript.objects.filter(pk=post_id))
    return render(request, "Full2.html", {"article": article})

