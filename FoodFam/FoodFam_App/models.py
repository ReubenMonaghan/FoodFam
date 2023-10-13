from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    # profile_picture = models.ImageField()


