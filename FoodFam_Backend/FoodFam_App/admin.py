from django.contrib import admin
from . models import *


admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Group)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(MeasurementUnit)
