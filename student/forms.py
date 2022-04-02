from django import forms
from .models import *


class studentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

class UpdatestudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = "__all__"

class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = "__all__"