from django.contrib import admin
from .models import Funny_Videos
from rangefilter.filter import DateRangeFilter
# Register your models here.


class Register(admin.ModelAdmin):
    list_display=['title','on_posted']
    search_field=['title','on_posted']
    list_filter=(('on_posted',DateRangeFilter),
    )


admin.site.register(Funny_Videos,Register)
