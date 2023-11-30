from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ingredient, MeasurementUnit, RecipeIngredient, Recipe, Comment, Rating, Group

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ['id', 'name']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    # ingredient and measurement_unit are nested serializers
    ingredient = IngredientSerializer()
    measurement_unit = MeasurementUnitSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'measurement_unit', 'quantity']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipe = serializers.ReadOnlyField(source='recipe.id')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'date_created', 'recipe', 'user']


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipe = serializers.ReadOnlyField(source='recipe.id')
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'recipe', 'user']


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    recipe_ingredients = RecipeIngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'recipe_ingredients', 'instructions', 'date_created', 'date_updated',
                  'owner', 'comments', 'ratings']



class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    ratings = serializers.PrimaryKeyRelatedField(many=True, queryset=Rating.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'recipes', 'comments', 'ratings']







class GroupSerializer(serializers.ModelSerializer):
    admins = serializers.ReadOnlyField(source='user.username')
    members = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'description', 'date_created', 'admins', 'members']

