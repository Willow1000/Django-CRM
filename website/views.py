from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['first_name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in')
            return redirect(reverse('home'))
        else:
            messages.warning(request,'Invalid name or password. Please try again')
            return redirect(reverse('home'))
    return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect(reverse('home'))

def register_user(request):
    return render(request,'register.html',{})