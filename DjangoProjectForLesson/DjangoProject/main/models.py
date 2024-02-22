from django.db import models
from .models import  *
from django.urls import reverse

# Create your models here.
class Python(models.Model):
    Title = models.CharField('Название' , max_length= 60)
    Article = models.TextField('Статья')
    ExampleImage = models.ImageField(upload_to='main/static/main/image')

    def __str__(self):
        return self.Article

class JavaScript(models.Model):
    Title = models.CharField('Название' , max_length= 60)
    Article = models.TextField('Статья')
    ExampleImage = models.ImageField()

    def __str__(self):
        return self.Article


