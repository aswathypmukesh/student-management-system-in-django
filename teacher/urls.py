from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.teacher_login,name="teacher_login" ),
    path('register/',views.teacher_register,name="teacher_register"),

]