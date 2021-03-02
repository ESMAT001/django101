from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','fname','last_name','date_of_birth','email','image']