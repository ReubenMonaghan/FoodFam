from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Profile(models.Model):
    # use auth_user for username, password, email and other details in the table.
    # use this model only for items not already in the auth_user
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    user = models.ForeignKey('auth.user', related_name='profile', on_delete=models.CASCADE)


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.JSONField()
    instructions = models.TextField(max_length=4000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.user', related_name='recipes', on_delete=models.CASCADE)


class Comment(models.Model):
    # check the on_delete settings for these
    text = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey('Recipe', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user', related_name='comments', on_delete=models.CASCADE)


class Rating(models.Model):
    # check the on_delete settings for these
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    recipe = models.ForeignKey('Recipe', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user', related_name='ratings', on_delete=models.CASCADE)


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    description = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)
    # https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
    admins = models.ManyToManyField('auth.user', related_name='group_admins')
    members = models.ManyToManyField('auth.user', related_name='group_members')
