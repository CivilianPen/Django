from django.db import models
from .models import  *
from django.urls import reverse

# Create your models here.
class Python(models.Model):
    Title = models.CharField('Название' , max_length= 60)
    Article = models.TextField('Статья')
    ExampleImage = models.ImageField(upload_to='main/static/main/image')

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("python", kwargs={"post_id": self.id})


class JavaScript(models.Model):
    Title = models.CharField('Название' , max_length= 60)
    Article = models.TextField('Статья')
    ExampleImage = models.ImageField(upload_to='main/static/main/image')

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("javascript", kwargs={"post_id": self.id})

class Reviews(models.Model):
    UserName = models.CharField('ИМЯ',max_length=16)
    Review = models.CharField('ОТЗЫВ',max_length=1600)
