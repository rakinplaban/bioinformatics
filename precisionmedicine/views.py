from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# methods I made.
from .forms import Patient_form,Disease_form
from .models import Patient,User,Disaese

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        patient_form = Patient_form()
        add_disese = Disease_form()
        patiants = Patient.objects.all().order_by('-id')
        diseases = Disaese.objects.all().order_by('-id')
        if request.method=="POST":
            patient_form = Patient_form(request.POST)

            if patient_form.is_valid():
                instance = patient_form.save(commit=False)
                instance.doctor = request.user
                instance.save()
                patient_form = Patient_form()

                return redirect("index")

            add_disese = Disease_form(request.POST)

            if add_disese.is_valid():
                instance = add_disese.save(commit=False)
                instance.save()
                add_disese = Disease_form()

                return redirect("index")

        return render(request,"precisionmedicine/index.html",{
            "patient_form" : patient_form,
            "patients" : patiants,
            "diseases" : diseases,
            "add_disease" : add_disese,
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def delete_patient(request,id):
    patient = Patient.objects.get(pk=id).delete()
    return redirect("index")

def delete_disease(request,id):
    disease = Disaese.objects.get(pk=id).delete()
    return redirect("index")

@csrf_protect
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "precisionmedicine/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "precisionmedicine/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@csrf_protect
def register(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            return render(request, "precisionmedicine/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.full_name = full_name
            user.save()

            # group = Group.objects.get(name="publisher")
            # user.groups.add(group)
        except IntegrityError:
            return render(request, "precisionmedicine/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "precisionmedicine/register.html")


def profile(request,id):
    id = request.user.id
    return render(request,"precisionmedicine/profile.html",{
            'id' : id
        })


def search(request):
    if request.method == "GET":
        search = request.GET['q']
        
        try:
            # diseases = Disaese.objects.get(name__icontains=search)
            # patient = diseases.patient.all().order_by('-id')
            patients = Patient.objects.filter(name__icontains=search)
        except ObjectDoesNotExist:
            return render(request,"precisionmedicine/index.html",{
            "message" : "No Result Found!",
            # "diseases" : Disaese.objects.all(),
        })
           
        return render(request,"precisionmedicine/index.html",{
            "search" : search,
            "patients" : patients,
            # "diseases" : Disaese.objects.all(),
        })
