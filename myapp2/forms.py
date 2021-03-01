from django import forms
from .models import students

class StudentForm(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','fname','last_name','date_of_birth','email','image']