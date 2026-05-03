from django.shortcuts import render,redirect,get_object_or_404
from tasks.models import*
from tasks.forms import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.contrib import messages

def register_page(request):
    
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=CustomUserInfoModel.objects.create_user(
            full_name=full_name,
            username=username,
            email=email,
            password=password,
            )
            
            if user:
                return redirect('login_page')
            else:
                print("Both password not match")
            
    
    return render(request,'register.html')


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('home_page')
        else:
            print('invalid')
    return render(request,'login.html')

@login_required
def home_page(request):
    return render(request,'home.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')
@login_required
def task_list(request):
    current_user=request.user
    task_data = TaskModel.objects.filter(created_by=current_user)
    context={
        'task_data' : task_data
    }
    
    return render(request,'task_list.html',context)


@login_required

def add_task(request):
    if request.method=='POST':
        form_data = TaskForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            return redirect('task_list')
    form_data=TaskForm()
    
    context={
        'form_data' : form_data,
        'form_title' : 'add task info',
        'btn_name' : 'add task',
    }
    return render(request, 'master/base-form.html',context)


@login_required

def update_task(request,t_id):
    task_data = get_object_or_404(TaskModel,id=t_id)
    
    if request.method=='POST':
        form_data = TaskForm(request.POST,instance=task_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            return redirect('task_list')
    else:
             form_data=TaskForm(instance=task_data)
        
    context={
            'form_data' : form_data,
            'form_title' : 'update task info',
            'btn_name' : 'update task',
        }
    return render(request,'master/base-form.html',context)


@login_required
def delete_task(request,t_id):
    get_object_or_404(TaskModel,id=t_id).delete()
    return redirect('task_list')
@login_required
def view_task(request,t_id):
    task_data = get_object_or_404(TaskModel,id=t_id)
    context={
        'task_data' : task_data
    }
    return render(request,'task-detail.html',context)

@login_required
def profile_page(request):

    return render(request,'profile.html')
@login_required
def update_profile(request):
    
    try:
        user_data = request.user.user_profile
    except ProfileModel.DoesNotExist:
        user_data = None
    if request.method == 'POST':
        form_data = UpdateProfileForm(
            request.POST, 
            request.FILES,
            instance=user_data
        )
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('profile_page')
    form_data = UpdateProfileForm(instance=user_data)
    context={
        'form_data'  : form_data,
        'form_title' : 'Update profile info',
        'btn_name'   : 'update'
    }

    return render(request,'master/base-form.html',context)



def product_list(request):
    product_data = ProductModel.objects.filter(created_by=request.user)
    context={
        'product_data':product_data
    }
    return render(request,'product_list.html',context)


def add_product(request):
    
    if request.method=='POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.created_by=request.user
            form_data.total_amount=form_data.price*Decimal(form_data.qty)
            form_data.save()
            return redirect('product_list')
    form_data = ProductForm()
    
    context={
        'form_data' : form_data,
        'form_title' : 'add product',
        'form_btn' : 'add product',
    }
    
    return render(request,'master/base-form.html',context)


def update_product(request,id):
    try:
        product_data = ProductModel.objects.get(id=id)
    except ProductModel.DoesNotExit:
        product_data=None
    if request.method=='POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.created_by=request.user
            form_data.total_amount=form_data.price*Decimal(form_data.qty)
            form_data.save()
            return redirect('product_list')
        
    form_data = ProductForm()
    
    context={
        'form_data' : form_data,
        'form_title' : 'add product',
        'form_btn' : 'add product',
    }
    
    return render(request,'master/base-form.html',context)
    






            