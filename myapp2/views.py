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
    text=request.GET.get('text')
    page=request.GET.get('page')
    student_list=Students.objects.filter(name__icontains=text)
    p=None
    if student_list:
        pagenation=Paginator(student_list,4)
        student_list=pagenation.get_page(page)
        end=student_list.has_previous()
        s=student_list
        p={
            "has_previous":student_list.has_previous(),
            'has_next':student_list.has_next(),
            'start_index':student_list.start_index(),
            'num_pages':student_list.paginator.num_pages,
            'number':student_list.number
        }
        if p['has_previous']:
            p.update({
                'previous_page':student_list.previous_page_number(),
                'previous_page_number':student_list.previous_page_number()
            })
        
        if p['has_next']:
            p.update({
                'next_page':student_list.next_page_number(),
                'next_page_number' :student_list.next_page_number()
            })


    # print((s.next_page_number()))
    # print(p)
    student_list=serializers.serialize('json',student_list)
    
    return JsonResponse({'data':student_list,'pagenation':p if p else {} })


@login_required(login_url=login_url)
def all_students_view(request):
    students_list=Students.objects.all()

    pagenation=Paginator(students_list,4)

    students_list=pagenation.get_page(request.GET.get('page'))
    # print(students_list[0].image)
    return render(request,'myapp2/index.html',{'students_list':students_list,
    'request':request})


@login_required(login_url="../"+login_url)
def student(request,id):
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
def add_student(request):
    # print(request.FILES)
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form =StudentForm()
    context={
        'form':form
    }
    return render(request,'myapp2/add_student.html',context)

@login_required(login_url="../"+login_url)
def update_student(request,id):
    print(request.FILES)
    try:
        data=Students.objects.get(id=id)
        form = StudentForm(request.POST or None, request.FILES or None ,  instance=data)
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
def delete_student(request,id):
    data=Students.objects.get(id=id)
    context={}
    if data:
        if request.method == "POST":
            data.delete()
            return redirect('../')
    else:
        context={'not_found':'student not found'}
    
    return render(request,'myapp2/confirmation.html',context)



def user_login(request):
    # print(request.user.is_anonymous)
    if not request.user.is_anonymous:
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


def logout_user(request):
    
    if request.method=="POST":
        logout(request)
        return redirect('../')
    return render(request,'myapp2/confirmation.html',{})


def user_register(request):
    if not request.user.is_anonymous:
        return redirect('../')
    form=UserRegisterForm()

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    # print(dir(form))
    return render(request,'myapp2/register.html',{'form':form})