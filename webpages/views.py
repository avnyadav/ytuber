from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    #extracting slider ifnformation
    sliders = Slider.objects.all()

    #extracting all team data
    teams = Team.objects.all()

    #extracting featured youtuber
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    
    #extarcting latest youtubers
    latest_on_board_youtubers = Youtuber.objects.order_by('-created_date').all()

    #preparing data for the template
    data = {
        'sliders': sliders,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        "latest_on_board_youtubers":latest_on_board_youtubers,
    }

    return render(request,'webpages/home.html',data)


def about(request):
    #extarcting all tea deatil to showcase on the about page
    teams = Team.objects.all()
    data = {

    'teams':teams,

    }
    return render(request,'webpages/about.html',data)

def services(request):
    #implimenting services page based on the request
    return render(request,'webpages/services.html')


def contact(request):
    #implimenting contact page based on the request
    tuber_data  = Youtuber.objects.all()
    data = {
        'tuber':tuber_data
    }
    
    return render(request,'webpages/contact.html',data)