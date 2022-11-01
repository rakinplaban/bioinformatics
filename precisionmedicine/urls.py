from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view,name="logout"),
    path("register",views.register,name="register"),
    path('delete/<id>',views.delete_patient,name="delete_patient"),
    path('delete_dis/<id>',views.delete_disease,name="delete_disease"),
    path("search/",views.search,name="search"),
]

