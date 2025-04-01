from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, default='')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])


class RecipeIngredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ingredients"
    )
    

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name="images"
                                )