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
        #extracting username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        #authenticate the user
        user = auth.authenticate(username=username, password=password)

        #if user is not None means user is authenticated
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):

    #check if the request is a post request 
    if request.method=="POST":
        #extracting data from the form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        user_name = request.POST['user-name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        #started validating the data
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                #checking if email is used or not
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    #validation successful hence creating the user
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
    #if the request is not a post request
    return render(request, 'accounts/register.html')

#redirecting to the login page if the user is not logged in and trying to access the dashboard
@login_required(login_url='login')
def dashboard(request):
    #extracting all youtuber information to show at the dashboard
    youtubers  = Youtuber.objects.order_by('-created_date').all()
    data = {
        'youtubers': youtubers
    }
    return render(request, 'accounts/dashboard.html',data)


def logout_user(request):
    #logging out the user
    logout(request)
    messages.success(request, 'You are now logged out')
    #once logout is complete redirecting to the home page
    return redirect('home')