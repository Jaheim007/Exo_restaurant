from email.mime import message
from django.db import models

class Social(models.Model):
    icon = models.FileField()
    email = models.EmailField(max_length=200)
    fb_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)

    created_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, )
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.icon

# Create your models here.
