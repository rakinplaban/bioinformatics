from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=70,null=True)
    # username = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
