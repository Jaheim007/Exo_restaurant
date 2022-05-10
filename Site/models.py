import email
from xml.parsers.expat import model
from django.db import models

class SiteInfo(models.Model):
   nom = models.CharField(max_length=255)
   section_image_blog = models.FileField()
   section_blog_libele = models.CharField(max_length=255)
   menu_description = models.TextField(max_length=500)
   addresse = models.CharField(max_length=255)
   dial_code = models.CharField(max_length=4)
   telephone = models.CharField(max_length=10)
   email = models.EmailField(max_length=255)
   copy_right = models.TextField(max_length=500)
   section_image_news = models.FileField()
   section_description = models.TextField(max_length=500)

   created_at = models.DateTimeField(auto_now=True, null=True)
   delete_at = models.DateTimeField(null=True, )
   updated_at = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
     return self.nom
    

# Create your models here.
