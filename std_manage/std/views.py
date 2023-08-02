from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
    std=Student.objects.all()
    return render(request,"std/home.html",{'std':std})

def std_add(request):
    if request.method=='POST':
        print("Added Successfully")
        # accrepting user input
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_contact=request.POST.get("std_contact")
        std_address=request.POST.get("std_address")


        # create an object for models

        s = Student()
        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.contact = std_contact
        s.address = std_address

        s.save()
        return redirect("/")

    return render(request,"std/add_std.html",{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/")


def update_std(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,"std/update_std.html",{'std':std})

def do_update_std(request,roll):
     std_roll=request.POST.get("std_roll")
     std_name=request.POST.get("std_name")
     std_email=request.POST.get("std_email")
     std_contact=request.POST.get("std_contact")
     std_address=request.POST.get("std_address")

     std = Student.objects.get(pk=roll)

     std.roll=std_roll
     std.name=std_name
     std.email=std_email
     std.contact=std_contact
     std.address=std_address 

     std.save()
     return redirect("/")