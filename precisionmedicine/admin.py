from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
# Register your models here.

def User_display(ModelAdmin):
    list_display = ("id","username","password")