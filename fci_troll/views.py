from django.shortcuts import render
from .models import Fci_Troll
from bangla_jokes.models import Bangla_Jokes
from engineering_jokes.models import Engineering_Jokes
from funny_videos.models import Funny_Videos
from programming_jokes.models import Programming_Jokes
from others.models import Logo
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

l=Logo.objects.last()
def fci_troll(request):
    post=Fci_Troll.objects.all().order_by('-on_posted')

    paginator=Paginator(post,5)
    page=request.GET.get('page')

    total_content=paginator.get_page(page)
    fci=Fci_Troll.objects.order_by('?')[:4]
    search=request.GET.get('q')
    if search:
        total_content=post.filter(Q(title__icontains=search))
    context={'contents':total_content,
    'category':'FCI Troll',
    'fci':fci,
    'l':l,
    'title':'FCI Troll',
    }
    return render(request,'fci_troll.html',context)
def fci(request,pk):
    content=Fci_Troll.objects.get(pk=pk)
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
