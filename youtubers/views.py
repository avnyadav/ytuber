from gc import get_objects
from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.
from collections import namedtuple


def youtubers(request):
    #extracting all youtuber details
    tubers = Youtuber.objects.order_by("-created_date")

    #extracting all unique cities name available in the database
    city_search  = Youtuber.objects.values_list('city',flat=True).distinct()

    #extracting all unique camera type available in the database
    camera_type_search  = Youtuber.objects.values_list('camera_type',flat=True).distinct()

    #extracting all unique category available in the database
    category_search  = Youtuber.objects.values_list('category',flat=True).distinct()
    
    #preparing data for the template
    data={
        "tubers": tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request, "youtubers/youtubers.html", data)


def youtubers_detail(request, id:int):
    #extracting all youtuber details
    tuber = get_object_or_404(Youtuber, pk=id)
    tuber_key="tuber"

    #preparing data for template
    data ={
        tuber_key: tuber

    }

    return render(request, "youtubers/youtuber_detail.html", data)

def search(request):
    #extracting all youtuber details
    tubers = Youtuber.objects.order_by("-created_date")

    #extracting all unique cities name available in the database
    city_search  = Youtuber.objects.values_list('city',flat=True).distinct()

    #extracting all unique camera type available in the database
    camera_type_search  = Youtuber.objects.values_list('camera_type',flat=True).distinct()

    #extracting all unique category available in the database
    category_search  = Youtuber.objects.values_list('category',flat=True).distinct()
    
    #filter youtuber detail based on keyword send in request
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    #filtering youtuber record based on city given in request
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    #filtering youtuber record based on camera type given in request
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    #filtering youtuber record based on category given in request
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    #preparing data for the template 
    data ={
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,

    }
    return render(request, "youtubers/search.html", data)


    

