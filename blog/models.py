from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=144)
    slug=models.CharField(max_length=330,default=slugify(title))
    timeStamp=models.DateTimeField(blank=True,default=now)
    content=models.TextField()
    img=models.CharField(max_length=456,default='')
    tags=models.CharField(max_length=456,default='')
    desc=models.CharField(max_length=456,default='')
    visibility=models.BooleanField(default=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return f'/blog/{self.slug}/'

class Comment(models.Model):
    sno= models.AutoField(primary_key=True)
    content=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username
