from django.forms import ModelForm
from .models import Recipe, RecipeImage

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'