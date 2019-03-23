from django.contrib import admin
from .models import Programming_Jokes
from rangefilter.filter import DateRangeFilter
# Register your models here.

class Register(admin.ModelAdmin):
    list_display=['title','picture','on_posted']
    search_field=['title','picture','on_posted']
    list_filter=(('on_posted',DateRangeFilter),
    )
admin.site.register(Programming_Jokes,Register)
