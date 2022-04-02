from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home" ),
    path('add/', views.add,name="add" ),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('mark/', views.add_mark, name="mark"),
    path('login/', views.student_login,name="student_login" ),
    path('logout/', views.student_logout,name="student_logout" )
]