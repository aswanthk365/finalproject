from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . forms import UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"This username alredy taken")
                return redirect('Accounts:registration')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"This"+ email +"alredy taken")
                return redirect('Accounts:registration')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                user.save()
                messages.success(request,'sucessfuly registered')
                return redirect('Accounts:login')
        else:
            messages.info(request,"password not matched")
            return redirect('Accounts:registration')
    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            messages.info(request,"susfully logged in " + username)
            return redirect('index')
        else:
            messages.info(request,"Deatails are invailded")
            print("wrong")
            return redirect('Accounts:login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        if u_form.is_valid():          
            u_form.save()                
            messages.success(request, f'Your profile has been updated!')
            return redirect('/')
    else:
        print('else')   
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html',{'u_form':u_form})
