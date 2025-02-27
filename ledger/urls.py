from django.urls import path

from .views import recipe_list_view, recipe_detail_view

urlpatterns = [
    path('recipes/list', recipe_list_view, name='recipe_list'),
    path('recipe/1', recipe_detail_view, name='recipe_detail'),
]

app_name = 'ledger'