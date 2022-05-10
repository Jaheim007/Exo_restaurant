from django.db import models

class Banner(models.Model):
    img = models.FileField()

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True,)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.img

# Create your models here.
