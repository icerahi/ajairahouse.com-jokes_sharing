from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
from bangla_jokes.models import Bangla_Jokes
from engineering_jokes.models import Engineering_Jokes
from fci_troll.models import Fci_Troll
from funny_videos.models import Funny_Videos
from programming_jokes.models import Programming_Jokes
from others.models import Logo

from django.db.models import Q
from itertools import chain


l=Logo.objects.last()
def home(request):
    bangla_jokes=Bangla_Jokes.objects.last()
    engineering_jokes=Engineering_Jokes.objects.last()
    fci_troll=Fci_Troll.objects.last()
    funny_videos=Funny_Videos.objects.last()
    programming_jokes=Programming_Jokes.objects.last()


    bangla=Bangla_Jokes.objects.order_by('?')[0]
    engineer=Engineering_Jokes.objects.order_by('?')[0]
    fci=Fci_Troll.objects.order_by('?')[0]
    funny=Funny_Videos.objects.order_by('?')[0]
    programming=Programming_Jokes.objects.order_by('?')[0]

    search=request.GET.get('q')

    context={'bangla_jokes':bangla_jokes,
    'engineering_jokes':engineering_jokes,
    'fci_troll':fci_troll,
    'funny_videos':funny_videos,
    'programming_jokes':programming_jokes,

    "l":l,

     'bangla':bangla,
     'engineer':engineer,
     'fci':fci,
     'funny':funny,
     'programming':programming}


    return render(request,'home.html',context)
