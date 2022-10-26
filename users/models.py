from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    sno= models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username