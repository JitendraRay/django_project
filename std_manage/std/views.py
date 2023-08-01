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
