from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Comment(models.Model):
    # check the on_delete settings for these
    text = models.CharField(max_length=280)
    date_created = models.DateField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)


class Rating(models.Model):
    # check the on_delete settings for these
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=50)
    Description = models.CharField(max_length=280)
    date_created = models.DateField()
    admins = models.ManyToManyField('Users', related_name='admin_groups')
