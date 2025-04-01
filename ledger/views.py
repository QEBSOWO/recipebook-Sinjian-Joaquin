from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Ingredient, Recipe

from .forms import RecipeForm, RecipeImageForm

from django.urls import reverse_lazy

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

@login_required
def recipe_add_view(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('ledger:recipe_detail', pk=recipe.pk)
        
    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()

    ctx = {
        "Recipes": recipes,
        "Ingredients": ingredients,
        "Form": form
    }

    return render(request, 'recipe_add.html', ctx)

@login_required
def recipe_update_view(request, pk):
    form = RecipeImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = Recipe.objects.get(pk=pk)
            recipe_image.save()
            return redirect('ledger:recipe_detail', pk=recipe_image.recipe.pk)
        
    recipes = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.all()

    ctx = {
        "Recipes": recipes,
        "Ingredients": ingredients,
        "Form": form
    }

    return render(request, 'recipe_update.html', ctx)
