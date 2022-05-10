from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class Site(admin.ModelAdmin):
    list_display = ('nom', 'section_image_blog', 'section_blog_libele', 'menu_description', 'addresse', 'dial_code', 'telephone', 'email', 'copy_right', 'section_image_news','section_description' )
    
    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')  

admin.site.register(SiteInfo, Site)

# Register your models here.
