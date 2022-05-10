from django.db import models

class Menu(models.Model):
    nom_plat = models.CharField(max_length=255)
    Prix = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom_plat

# Create your models here.
