from django.db import models

class SiteInfo(models.Model):
    nom = models.CharField(max_length=255)
    section_blog_image = models.FileField()
    section_blog_libele = models.CharField(max_length=255)
    menu_description = models.TextField(max_length=500)
    addresse = models.CharField(max_length=255)
    dial_code = models.CharField(max_length=4)
    telephone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    copyright = models.TextField(max_length=500)
    section_image_news = models.FileField()
    section_description_news = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)
   
    def __str__(self):
        return self.nom
    

class Banner(models.Model):
    img = models.FileField()

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)
    

class Blog(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    img = models.FileField()
    
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.nom
   
class PlatFavoris(models.Model):
    nom = models.CharField(max_length=255)
    img = models.FileField()

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.nom


class Menu(models.Model):
    nom_plat = models.CharField(max_length=255)
    Prix = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_plat

# Create your models here.
