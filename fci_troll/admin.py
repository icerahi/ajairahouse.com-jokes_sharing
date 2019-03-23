from django.contrib import admin
from .models import Fci_Troll
from rangefilter.filter import DateRangeFilter
# Register your models here.

class Register(admin.ModelAdmin):
    list_display=['title','picture','on_posted']
    search_field=['title','picture','on_posted']
    list_filter=(('on_posted',DateRangeFilter),
    )
admin.site.register(Fci_Troll,Register)
