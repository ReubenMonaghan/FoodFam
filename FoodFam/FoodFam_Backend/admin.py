from django.contrib import admin
from . models import *

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 1  # Number of empty forms to display

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('title', 'owner', 'date_created', 'date_updated')
    search_fields = ['title', 'owner__username']  # Enable searching by title and owner username


admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Group)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(MeasurementUnit)
