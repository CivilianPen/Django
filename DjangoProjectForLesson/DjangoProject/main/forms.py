from django import forms
from .models import *


class AddPostForm(forms.Form):
    UserName = forms.CharField(max_length=16, label="Имя")
    Review = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Отзыв")
