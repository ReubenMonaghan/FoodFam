# Generated by Django 4.2.6 on 2023-10-22 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodFam_Backend', '0007_alter_comment_recipe_alter_rating_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(related_name='group_admins', to=settings.AUTH_USER_MODEL),
        ),
    ]
