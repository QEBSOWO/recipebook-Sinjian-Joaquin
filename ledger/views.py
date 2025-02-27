from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.

'''
recipe1 = {
    "name": "Recipe 1",
    "ingredients": [
        {
            "name": "tomato",
            "quantity": "3pcs"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "pork",
            "quantity": "1kg"
        },
        {
            "name": "water",
            "quantity": "1L"
        },
        {
            "name": "sinigang mix",
            "quantity": "1 packet"
        }
    ],
    "link": "/recipe/1"
}

recipe2 = {
    "name": "Recipe 2",
    "ingredients": [
        {
            "name": "garlic",
            "quantity": "1 head"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "vinegar",
            "quantity": "1/2cup"
        },
        {
            "name": "water",
            "quantity": "1 cup"
        },
        {
            "name": "salt",
            "quantity": "1 tablespoon"
        },
        {
            "name": "whole black peppers",
            "quantity": "1 tablespoon"
        },
        {
            "name": "pork",
            "quantity": "1 kilo"
        }
    ],
    "link": "/recipe/2"
}

recipes = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quanity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}
'''

def recipe_list_view(request):
    print(request)

    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    ctx = {
        "Recipes": recipes,
        "Ingredients": ingredients
    }

    return render(request, "recipe_list.html", ctx)

def recipe_detail_view(request, thing):
    print(request)

    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    ctx = {
        "Recipes": recipes,
        "Ingredients": ingredients
    }

    return render(request, "recipe_detail.html", ctx)