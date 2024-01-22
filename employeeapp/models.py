from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    dob = models.DateField()