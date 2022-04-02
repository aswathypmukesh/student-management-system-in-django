from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    email_id = models.CharField(max_length=100)
    dob = models.DateField()
    standard = models.CharField(max_length=100)
    active = models.BooleanField(default = True)

class Mark(models.Model):
    subject = models.CharField(max_length=100)
    mark = models.IntegerField(default=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    active = models.BooleanField(default = True)
    
    