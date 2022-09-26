from django.db import models

# Create your models here.

class Employee(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=255)
    Department = models.CharField(max_length=255)


