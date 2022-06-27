from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.db import IntegrityError

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,"precisionmedicine/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request,'precisionmedicine/login.html',{
                "message" : "Sorry, the username or password may be invalid!"
            })

    else:
        return render(request,"precisionmedicine/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if(password != confirm_password):
            return render(request,"precisionmedicine/register.html",{
                'message' : "Sorry! Password didn't matche."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })

        login(request,user)
        return HttpResponseRedirect(reverse("profile",kwargs={id: request.user.id}))

    else:
        return render(request,"precisionmedicine/register.html")


def profile(request,id):
    id = request.user.id
    return render(request,"precisionmedicine/profile.html",{
            'id' : id
        })
