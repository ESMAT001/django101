from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
login_url='login/'

# @login_required(login_url=login_url)
def AllStudentsView(request):
    students_list=Students.objects.all()
    return render(request,'myapp2/index.html',{'students_list':students_list,
    'request':request})


# @login_required(login_url=login_url)
def Student(request,id):
    Student_info=Students.objects.get(id=id)
    if Student_info:
        context={
            'student_info':Student_info
        }
    else:
        context={
            'not_found':'student not found'
        }
    return render(request,'myapp2/student.html',context)


@login_required(login_url=login_url)
def AddStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form =StudentForm()
    context={
        'form':form,
        'title':"AddStudent"
    }
    return render(request,'myapp2/add_student.html',context)

@login_required(login_url=login_url)
def UpdateStudent(request,id):
    try:
        data=Students.objects.get(id=id)
        form = StudentForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('../')
        context={
            'form':form
        }
      
    except:
        context={
            'not_found':'student not found'
        }
    
    return render(request,'myapp2/add_student.html',context)

@login_required(login_url=login_url)
def DeleteStudent(request,id):
    data=Students.objects.get(id=id)
    context={}
    if data:
        if request.method == "POST":
            data.delete()
            return redirect('../')
    else:
        context={'not_found':'student not found'}
    
    return render(request,'myapp2/confirmation.html',context)



def UserLogin(request,next):
    print(next)
    return render(request,'myapp2/login.html',{})