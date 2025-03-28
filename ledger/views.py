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

@login_required
def recipe_add_view(request):
    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()
    ctx = { "Recipies": recipes, "Ingredients": ingredients }
    if(request.method == "POST"):
        r = Recipe()
        r.name = request.POST.get('task_name')
        r.due_date = request.POST.get('task_due')
        r.taskgroup = TaskGroup.objects.get(pk=request.POST.get('taskgroup'))
        r.save()
        return render(request, 'task_list.html', ctx)
    else:
        return render(request, 'task_list.html', ctx)
