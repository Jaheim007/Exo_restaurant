import email
from email import message
from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.nom

# Create your models here.
