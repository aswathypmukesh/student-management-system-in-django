from django.contrib import admin

# from student.views import student
from .models import *
# Register your models here.

admin.site.register([Student,Mark])
