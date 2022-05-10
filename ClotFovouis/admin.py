from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class FavContent(admin.ModelAdmin):
    list_display = ('nom', 'img' )

    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">') 


admin.site.register(Fav, FavContent)

# Register your models here.
