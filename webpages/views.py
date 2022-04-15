from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    latest_on_board_youtubers = Youtuber.objects.order_by('-created_date').all()
    data = {
        'sliders': sliders,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        "latest_on_board_youtubers":latest_on_board_youtubers,
    }
    return render(request,'webpages/home.html',data)


def about(request):
    teams = Team.objects.all()
    data = {

    'teams':teams,

    }
    return render(request,'webpages/about.html',data)

def services(request):
    return render(request,'webpages/services.html')


def contact(request):
    tuber_data  = Youtuber.objects.all()
    data = {
        'tuber':tuber_data
    }
    
    return render(request,'webpages/contact.html',data)