from django.contrib import admin
from .models import Bangla_Jokes
from rangefilter.filter import DateRangeFilter,DateTimeRangeFilter
# Register your models here.


admin.site.site_title="AjairaHouse";
admin.site.site_header="Team IceCream Production";

class Register(admin.ModelAdmin):
    list_display=['title','picture','on_posted']
    search_field=['title','picture','on_posted']
    list_filter=(('on_posted',DateRangeFilter),
    )
admin.site.register(Bangla_Jokes,Register)
