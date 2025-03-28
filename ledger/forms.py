from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.Form):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(forms.Form):
    class Meta:
        model = RecipeImage
        fields = '__all__'