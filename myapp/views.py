from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import items
from .forms import itemsForm
# Create your views here.
def index(request):
    items_list=items.objects.all()
    template=loader.get_template('myapp/index.html')
    context={
        'items_list':items_list,
    }
    return HttpResponse(template.render(context,request))

def shortcut(request):
    items_list=items.objects.all()
    context={
        'items_list':items_list,
        'with':'with render method',
    }

    return render(request,'myapp/index.html',context)

def itemsList(request):
    items_list=items.objects.all()
    context={
        'items_list':items_list,
    }
    return render(request,'myapp/index.html',context)


def item(request,item_id):
    item_info=items.objects.get(pk=item_id)
    context={
        'item_info':item_info
    }
    return render(request,'myapp/item_info.html',context)

def add_item(request):
    form =itemsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('../')
    
    return render(request,'myapp/items_form.html',{'form':form})


def update_item(request,id):
    item=items.objects.get(id=id)
    form =itemsForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('../../')
    
    return render(request,'myapp/items_form.html',{'form':form,'item':item})


def delete_item(request,id):
    item=items.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('../../')

    return render(request,'myapp/delete_form.html',{'item':item})