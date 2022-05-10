from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class Reseau(admin.ModelAdmin):
    list_display = ('email', 'fb_link', 'insta_link', 'twitter_link','icon')

    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">') 

admin.site.register(Social, Reseau)

# Register your models here.
