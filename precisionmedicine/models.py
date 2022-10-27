from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=70,null=True)
    # username = models.CharField(max_length=50)
    email = models.CharField(max_length=25)


class Patient(models.Model):
    GENDER = (
        ('M',"Male"),
        ('F',"Female"),
        ('O',"Others")
    )
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER,default='M')
    protine = models.CharField(max_length=8)

# class Medicine(models.Model):
#     name= models.CharField()