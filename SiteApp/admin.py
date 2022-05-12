from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class SiteContent(admin.ModelAdmin):
    list_display = ('nom','email','addresse','telephone','section_blog_libele', 'views', 'section_image_news', 'status')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.section_blog_image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'  
    
admin.site.register(SiteInfo, SiteContent)

@admin.register(Banner)
class BannerContent(admin.ModelAdmin):      
    list_display = ('views',)
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    



class BlogContent(admin.ModelAdmin):
    list_display = ('nom', 'description', 'img', 'status')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    
admin.site.register(Blog, BlogContent)

class PlatFavorisContent(admin.ModelAdmin):
    list_display = ('nom' , 'img')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    
admin.site.register(PlatFavoris, PlatFavorisContent)

class MenuContent(admin.ModelAdmin):
    list_display = ('nom_plat' ,'Prix', 'description', 'status')
    
admin.site.register(Menu, MenuContent)

# Register your models here.
