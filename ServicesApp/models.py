from django.db import models

class About(models.Model):
    libele = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    img = models.FileField()
    
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.libele
   
class News(models.Model):
    email = models.EmailField(max_length=254)

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.email
   
class Social(models.Model):
    email = models.EmailField(max_length=200)
    fb_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    icon = models.FileField()
    
    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, )
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.email
   
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
       return self.nom
   


# Create your models here.
