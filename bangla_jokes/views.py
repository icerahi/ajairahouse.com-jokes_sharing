from django.shortcuts import render
from .models import Bangla_Jokes
from engineering_jokes.models import Engineering_Jokes
from fci_troll.models import Fci_Troll
from funny_videos.models import Funny_Videos
from programming_jokes.models import Programming_Jokes
from others.models import Logo

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from itertools import chain

# Create your views here.
l=Logo.objects.last()
def bangla_jokes(request):
    r_content=Bangla_Jokes.objects.order_by('?')[:4]

    post=Bangla_Jokes.objects.all().order_by('-on_posted')
    paginator=Paginator(post,5)
    page=request.GET.get('page')

    all_content=paginator.get_page(page)

    search=request.GET.get('q')
    if search:
        all_content=Bangla_Jokes.objects.filter(Q(title__icontains=search))

    context={
    'contents': all_content,
    'category':'Bangla Jokes',
    'bangla':r_content,
    'l':l,
    'title':'Bangla Jokes'
    }
    return render(request,'bangla_jokes.html',context)



def bangla(request,pk):

    content=Bangla_Jokes.objects.get(pk=pk)

    bangla=Bangla_Jokes.objects.order_by('?')[0]
    engineer=Engineering_Jokes.objects.order_by('?')[0]
    fci=Fci_Troll.objects.order_by('?')[0]
    funny=Funny_Videos.objects.order_by('?')[0]
    programming=Programming_Jokes.objects.order_by('?')[0]



    context={
    'content':content,
    'bangla':bangla,
    'engineer':engineer,
    'fci':fci,
    'funny':funny,
    'programming':programming,
    'l':l,
    'title':content.title

     }


    return render(request,'single.html',context)
