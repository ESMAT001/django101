from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import students
from .forms import StudentForm
# Create your views here.
def AllStudentsView(request):
    students_list=students.objects.all()
    return render(request,'myapp2/index.html',{'students_list':students_list,
    'request':request})


def AddStudent(request):
   
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        print('before validation ')
        if form.is_valid():
           
            form.save()
        print(request.FILES,'-------file')
        print(form.errors)
    else:
        form =StudentForm()
        dir(form)
    return render(request,'myapp2/add_student.html',{'form':form})