# Generated by Django 4.2.6 on 2023-11-28 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFam_App', '0013_remove_recipe_ingredients_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
    ]