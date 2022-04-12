from django.urls import path

from . import views

urlpatterns=[
    path('',views.hire_tuber,name='hiretuber'),
 
]