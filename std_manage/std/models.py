from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.CharField(max_length=3)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=13)
    address=models.CharField(max_length=300)
