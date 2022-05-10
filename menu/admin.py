from django.contrib import admin
from .models import *

class MenuContent(admin.ModelAdmin):
    list_display = ('nom_plat', 'Prix', 'description')

admin.site.register(Menu, MenuContent)

# Register your models here.
