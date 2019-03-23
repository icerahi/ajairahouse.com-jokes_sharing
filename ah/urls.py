from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
app_name=(
'home'
'fci_troll'
'bangla_jokes',
'programming_jokes',
'engineering_jokes',
'funny_videos',

'others'

)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('fci_troll/',include('fci_troll.urls')),
    path('bangla_jokes/',include('bangla_jokes.urls')),
    path('programming_jokes/',include('programming_jokes.urls')),
    path('engineering_jokes/',include('engineering_jokes.urls')),
    path('funny_videos/',include('funny_videos.urls')),

    path('',include('others.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
