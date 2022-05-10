from django.db import models

class Blog(models.Model):
    img = models.FileField()
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True )
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.img

# Create your models here.
