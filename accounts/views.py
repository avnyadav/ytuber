import re
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import  messages, auth
from youtubers.models import Youtuber
# Create your views here.
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method=="POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        user_name = request.POST['user-name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=user_name, 
                                        password=password, 
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')

    return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    youtubers  = Youtuber.objects.order_by('-created_date').all()
    data = {
        'youtubers': youtubers
    }
    return render(request, 'accounts/dashboard.html',data)

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')