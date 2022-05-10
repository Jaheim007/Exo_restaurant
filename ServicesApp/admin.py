from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class AboutContent(admin.ModelAdmin):
    list_display = ('libele', 'description', 'img', 'status')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">')
    
admin.site.register(About, AboutContent)

admin.site.register(News) 

class ContactContent(admin.ModelAdmin):  
    list_display = ('nom', 'email', 'message', 'status')  
    
admin.site.register(Contact, ContactContent) 

class SocialContent(admin.ModelAdmin):  
    list_display = ('email', 'fb_link', 'insta_link', 'twitter_link', 'icon', 'status') 
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.image.url}" style = "height:100px; width:200px">') 
    
admin.site.register(Social, SocialContent) 


    
# Register your models here.
