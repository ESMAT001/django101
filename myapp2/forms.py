from django import forms
from .models import Students
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','fname','last_name','date_of_birth','email','image']
        widgets={
            'date_of_birth':forms.TextInput(attrs={
                "type":'date'
            })
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1' ,'password2']
        