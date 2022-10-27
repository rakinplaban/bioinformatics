from django.contrib import admin
from .models import User,Patient
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display = ("id","full_name","username","email")

class Patient_display(admin.ModelAdmin):
    list_display = ("id","name","age","gender","protine")

admin.site.register(User,User_display)
admin.site.register(Patient,Patient_display)
