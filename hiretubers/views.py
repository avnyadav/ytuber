import re
from django.shortcuts import render,redirect
from .models import HireTubers
from django.contrib import  messages

def hire_tuber(request):
    #if request is post request
    if request.method=="POST":
        #extracting data from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        phone_number = request.POST['phone_number']
        tuber_id = request.POST['tuber_id']
        user_id = request.POST['user_id']
        message = request.POST['message']

        #creating a hire tubers object
        hire_tubers = HireTubers(
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                state=state,
                                city=city,
                                phone_number=phone_number,
                                tuber_id=tuber_id,
                                user_id=user_id,
                                message=message)
        hire_tubers.save()
        #rediecting to home page
        messages.success(request, 'Your message has been sent!')
        return redirect('home')

        
        


