from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.

class recipe_list_view(ListView):

    model = Recipe
    template_name = 'recipe_list'


class recipe_detail_view(LoginRequiredMixin, DetailView):
    
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = ''

