from django.contrib import admin
from .models import User,Patient,Disaese
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display = ("id","full_name","username","email")

class Patient_display(admin.ModelAdmin):
    list_display = ("id","name","age","gender","protine")

class Disease_display(admin.ModelAdmin):
    list_display = ("id","name","root_protine","patient")

admin.site.register(User,User_display)
admin.site.register(Patient,Patient_display)
admin.site.register(Disaese,Disease_display)
