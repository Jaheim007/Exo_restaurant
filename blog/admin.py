from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class BlogContent(admin.ModelAdmin):
    list_display = ('nom', 'description', 'img')

    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">') 

admin.site.register(Blog, BlogContent)

# Register your models here.
