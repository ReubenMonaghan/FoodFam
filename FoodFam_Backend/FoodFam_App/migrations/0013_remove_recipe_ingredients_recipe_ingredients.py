# Generated by Django 4.2.6 on 2023-11-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFam_App', '0012_ingredient_measurementunit_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='FoodFam_App.recipeingredient'),
            preserve_default=False,
        ),
    ]
