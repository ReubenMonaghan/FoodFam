from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Profile(models.Model):
    # use auth_user for username, password, email and other details in the table.
    # use this model only for items not already in the auth_user
    #Learing oppertunity, use AWS S3 to store images.
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    user = models.ForeignKey('auth.user', related_name='profile', on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    # ForeignKey fields represent a many-to-one relationship; many RecipeIngredients-to-one Recipe
    # and many RecipeIngredients-to-one Ingredient and MeasurementUnit
    # https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/
    recipe = models.ForeignKey('Recipe', related_name='recipe_ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', related_name='ingredient', on_delete=models.CASCADE)
    measurement_unit = models.ForeignKey('MeasurementUnit', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    # I tried manytomany field below because a recipe can have many recipeingredients and a recipeingredient
    # could be in many recipes. I think this is wrong. I think a foreignkey is a onetomany relationship. one recipe
    # can have multiple recipeingredients.
    #ingredients = models.ManyToManyField(('Ingredient', 'measurement_unit'), through='RecipeIngredient')
    #ingredients = models.ForeignKey(RecipeIngredient, related_name='recipe_ingredients', on_delete=models.CASCADE)
    instructions = models.TextField(max_length=4000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.user', related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.group_name
