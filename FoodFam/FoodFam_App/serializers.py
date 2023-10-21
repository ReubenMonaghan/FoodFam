from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'date_created', 'date_updated', 'owner']

class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'recipes']