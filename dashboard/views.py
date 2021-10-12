from typing import OrderedDict
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User 
from django.contrib import messages

@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    customers_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()

            return redirect('dashboard-index')
    else:
        form = OrderForm()

    context = {
        'orders' : orders,
        'form' : form ,
        'products': products,
        'customer_count': customers_count,
        'order_count': order_count,
        'product_count': product_count,
    }
    return render(request,'dashboard/index.html',context)

@login_required
def staff(request):
    customers = User.objects.all()
    customers_count = customers.count()
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()

    context = {
        'customers' : customers,
        'customer_count' : customers_count,
        'order_count' : order_count,
        'product_count' : product_count,
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,pk):
    staff = User.objects.get(id = pk)
    context = {
        'staff' : staff 
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required
def product(request):
    customers_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    product_count = Product.objects.all().count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid() : 
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
        
    items = Product.objects.all()
    print(items)
    context = {
        'items' : items,
        'form' : form ,
        'customer_count' : customers_count,
        'order_count' : order_count,
        'product_count' : product_count,

    }
    return render(request,'dashboard/product.html',context)

@login_required
def product_delete(request,pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

@login_required
def product_update(request,pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid() : 
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form
    }
    return render(request,'dashboard/product_update.html',context)


@login_required
def order(request):
    orders = Order.objects.all()
    order_count = orders.count()
    customers_count = User.objects.all().count()
    product_count = Product.objects.all().count()

    context = {
        'orders' : orders,
        'customer_count': customers_count,
        'order_count' : order_count,
        'product_count': product_count,
    }
    return render(request,'dashboard/order.html',context)

