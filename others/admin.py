from django.contrib import admin
from .models import Logo

# Register your models here.

class Register(admin.ModelAdmin):
    list_display=['image' ]
    search_field=['image']

admin.site.register(Logo,Register)
