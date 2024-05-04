from django.contrib import admin
from .models import  *

# Register your models here.
@admin.register(Python)
class PythonAdmin(admin.ModelAdmin):
    list_display = ['Article','Title','ExampleImage']
    list_editable = ['Article','Title','ExampleImage']
    list_display_links = None

@admin.register(JavaScript)
class JavaScriptAdmin(admin.ModelAdmin):
    list_display = ['Article','Title','ExampleImage']
    list_editable = ['Article','Title','ExampleImage']
    list_display_links = None

@admin.register(Reviews)
class JavaScriptAdmin(admin.ModelAdmin):
    list_display = ['UserName','Review',]
    list_display_links = None
