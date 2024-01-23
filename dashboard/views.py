from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    workers=User.objects.all()
    worker_count=workers.count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'worker_count':worker_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'index.html',context)
@login_required(login_url='user-login')
def stats(request):
    return render(request,'topnav.html')
@login_required(login_url='user-login')
def staff(request):
    workers=User.objects.all()
    worker_count=workers.count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context={
        'workers':workers,
        'worker_count':worker_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'staff.html',context)
@login_required(login_url='user-login')
def products(request):
    items=Product.objects.all()
    worker_count=User.objects.all().count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('product')
    else:
        form = ProductForm()
    context={ 
        'items':items,
        'form':form,
        'worker_count':worker_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'product.html',context)
@login_required(login_url='user-login')
def order(request):
    orders=Order.objects.all()
    order_count=orders.count()
    worker_count=User.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'orders':orders,
        'worker_count':worker_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'order.html',context)

@login_required(login_url='user-login')
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('product')
    return render(request,'product_del.html')
@login_required(login_url='user-login')
def product_edit(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm(instance=item)
    context={
        'form':form
    }
    return render(request,'product_update.html',context)
@login_required(login_url='user-login')
def staff_detail(request,pk):
    worker=User.objects.get(id=pk)
    workers=User.objects.all()
    worker_count=workers.count()
    product_count=Product.objects.all().count()
    order_count=Order.objects.all().count()
    context={
        'worker':worker,
        'worker_count':worker_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'staff_detail.html',context)