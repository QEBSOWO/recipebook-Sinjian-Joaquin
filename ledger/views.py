from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.

def recipe_list_view(request):
    print(request)

    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    ctx = {
        "Recipes": recipes,
        "Ingredients": ingredients
    }

    return render(request, "recipe_list.html", ctx)

@login_required
def recipe_detail_view(request, pk):
    print(request)

    recipe = Recipe.objects.get(pk = pk)

    ctx = {
        "Recipe": recipe,
    }

    return render(request, "recipe_detail.html", ctx)
