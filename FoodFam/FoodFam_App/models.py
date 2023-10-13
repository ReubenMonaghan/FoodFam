from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    # profile_picture = models.ImageField()


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.JSONField()
    instructions = models.TextField(max_length=50)
    date_created = models.DateField()
    date_updated = models.DateField()
    owner = models.ForeignKey('Users', on_delete=models.CASCADE)