from django.db import models

# Create your models here.
# models.py

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    no_of_students = models.IntegerField()
    def __str__(self):
        return self.name