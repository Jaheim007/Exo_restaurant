from django.db import models

class News(models.Model):
    email = models.EmailField(max_length=254)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, )
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.email
# Create your models here.
