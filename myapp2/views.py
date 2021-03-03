from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Students
from .forms import StudentForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login,logout
from django.core import serializers
from django.core.paginator import Paginator
# Create your views here.
login_url='login-user/'


@login_required(login_url=login_url)
def search(request):
    text=request.GET['text']
    student_list=Students.objects.filter(name__icontains=text)
    student_list=serializers.serialize('json',student_list)
    
    return JsonResponse({'data':student_list})


@login_required(login_url=login_url)
def AllStudentsView(request):
    students_list=Students.objects.all()

    pagenation=Paginator(students_list,3)

    students_list=pagenation.get_page(request.GET.get('page'))
    # print(students_list[0].image)
    return render(request,'myapp2/index.html',{'students_list':students_list,
    'request':request})


@login_required(login_url="../"+login_url)
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
    # print(request.FILES)
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

@login_required(login_url="../"+login_url)
def UpdateStudent(request,id):
    print(request.FILES)
    try:
        data=Students.objects.get(id=id)
        form = StudentForm(request.POST or None,request.FILES or None,instance=data)
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

@login_required(login_url="../"+login_url)
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



def UserLogin(request):
    print()
    if str(request.user) != 'AnonymousUser':
        return redirect('../')
    context={}
    if request.method == "POST":
    
        user=authenticate(request,
                username=request.POST['username'],
                password=request.POST['password'])
        if user:
            login(request, user)
            
            to=request.GET['next'] if request.GET else '/'
            return redirect(to)
        else:
            context={
                'invalid':'invalid username or password'
            }
    return render(request,'myapp2/login.html',context)


def logoutUser(request):
    
    if request.method=="POST":
        logout(request)
        return redirect('../')
    return render(request,'myapp2/confirmation.html',{})


def user_register(request):
    if str(request.user) != 'AnonymousUser':
        return redirect('../')
    form=UserRegisterForm()

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    # print(dir(form))
    return render(request,'myapp2/register.html',{'form':form})