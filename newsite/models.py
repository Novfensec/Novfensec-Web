from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    message=models.TextField(max_length=None, default="")
    phone = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name