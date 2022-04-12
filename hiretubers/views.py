import re
from django.shortcuts import render,redirect
from .models import HireTubers
from django.contrib import  messages
#  tuber_id = models.IntegerField()
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255)
#     message = models.TextField()
#     user_id = models.IntegerField(blank=True,)
#     created_date = models.DateTimeField(blank=True,default = datetime.now)
# Create your views here.
def hire_tuber(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        phone_number = request.POST['phone_number']
        tuber_id = request.POST['tuber_id']
        user_id = request.POST['user_id']
        message = request.POST['message']
        hire_tubers = HireTubers(
            first_name=first_name,
            last_name=last_name,
            email=email,
            state=state,
            city=city,
            phone_number=phone_number,
            tuber_id=tuber_id,
            user_id=user_id,
            message=message
        )
        hire_tubers.save()

        messages.success(request, 'Your message has been sent!')
        return redirect('home')

        
        


