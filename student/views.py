from django.shortcuts import render, redirect

import student
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'GET':
        std = Student.objects.all()
        c = {
        'students': std,
        }
        return render(request, 'home.html',c)
    if request.method == 'POST':
        pass
    
def add(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.method == 'GET':
        form = studentForm()
    c = {
        'form': form,
    }
    return render(request, 'add.html',c)

def update(request, pk):
    std = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdatestudentForm(request.POST, instance=std)
        if form.is_valid():
            form.save() 
            return redirect('/')
    if request.method == 'GET':
        form = UpdatestudentForm( instance=std)
    c = {
        'form': form
    }
    return render(request, 'update.html', c)

def delete(request, pk):
    std = Student.objects.get(id=pk)
    if request.method == 'POST':
        std.delete()
        return redirect('/')
    return render(request, 'delete.html')

def profile(request, pk):
  
    if request.method == 'GET':
        std = Student.objects.get(id=pk)
        mark = Mark.objects.filter(student = std).first()
        c = {
            'std': std,
            'mark': mark
        }
        return render(request, 'profile.html',c)
   

def add_mark(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.method == 'GET':
        form = MarkForm()
    c = {
        'form': form,
    }
    return render(request, 'mark.html',c)

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        student = Student.objects.get(username=username,password=password)
        if student:
            request.session['student'] = username
            return redirect('profile', student.id)
        else:
            return HttpResponse('Please enter valid Username or Password.') 
    else:
        return render(request,'student_login.html')

def student_logout(request):
    del request.session['student']
    return redirect('student_login')

# def homestd(request):
#     if request.method == 'GET':
#         std = Student.objects.get()
#         c = {
#             'student': std,
#         }
#         return render(request, 'homestd.html',c)
    


 