from django.contrib import admin
from .models import Recipe, Category, Step, Ingredient

class StepInline(admin.StackedInline):
    model = Step
    extra = 1

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):

    inlines = [IngredientInline,StepInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(Step)
