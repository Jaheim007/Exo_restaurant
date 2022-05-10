from xml.parsers.expat import model
from django.db import models

class Fav(models.Model):
    nom = models.CharField(max_length=255)
    img = models.FileField()

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.nom

# Create your models here.
