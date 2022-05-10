from django.contrib import admin
from .models import *

class ContactContent(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message')

admin.site.register(Contact, ContactContent)

