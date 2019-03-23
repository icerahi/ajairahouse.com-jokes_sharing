from django.shortcuts import render
from .models import Funny_Videos
from bangla_jokes.models import Bangla_Jokes
from engineering_jokes.models import Engineering_Jokes
from fci_troll.models import Fci_Troll
from programming_jokes.models import Programming_Jokes
from others.models import Logo

from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
l=Logo.objects.last()
def funny_videos(request):
    post=Funny_Videos.objects.all().order_by('-on_posted')

    paginator=Paginator(post,5)
    page=request.GET.get('page')
    total_content=paginator.get_page(page)
    funny=Funny_Videos.objects.order_by('?')[:4]
    search=request.GET.get('q')
    if search:
        total_content=post.filter(Q(title__icontains=search))
    context={
    'contents':total_content,
    'category':'Funny Videos',
    'funny':funny,
    'l':l,
    'title':'Videos'

    }
    return render(request,'funny_videos.html',context)
def funny(request,pk):
    content=Funny_Videos.objects.get(pk=pk)
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
    'title':content.title,

     }


    return render(request,'single.html',context)
