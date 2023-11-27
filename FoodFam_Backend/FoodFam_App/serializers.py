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
    #ingredient = IngredientSerializer(source='Ingredient', many=True)
    bob = serializers.SerializerMethodField()

    #measurement_unit = MeasurementUnitSerializer(many=True)
    #measurement_units = serializers.SerializerMethodField()
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'bob'] # ['id', 'recipe', 'ingredient', 'measurement_unit', 'quantity', 'ingredient_items']

    def get_bob(self, obj):
        recipe_ingredients_query = Ingredient.objects.filter(id=obj.id)
        #measurement_units_query = MeasurementUnit.objects.filter(id=obj.id)
        #return self.measurement_unit
        serializer = IngredientSerializer(recipe_ingredients_query, many=True)
        #MeasurementUnitSerializer(measurement_units_query, many=True)
        return serializer.data

    def get_measurement_units(self, obj):
        measurement_units_query = MeasurementUnit.objects.filter(id=obj.id)
        serializer = MeasurementUnitSerializer(measurement_units_query, many=True)
        return serializer.data

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    ratings = serializers.PrimaryKeyRelatedField(many=True, queryset=Rating.objects.all())
    ingredients = RecipeIngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'date_created', 'date_updated',
                  'owner', 'comments', 'ratings']


class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    ratings = serializers.PrimaryKeyRelatedField(many=True, queryset=Rating.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'recipes', 'comments', 'ratings']

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


class GroupSerializer(serializers.ModelSerializer):
    admins = serializers.ReadOnlyField(source='user.username')
    members = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'description', 'date_created', 'admins', 'members']

