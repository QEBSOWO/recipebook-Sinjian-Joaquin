from django.urls import path

from .views import recipes_view, recipes_1_view, recipes_2_view

urlpatterns = [
    path('recipes/list', recipes_view, name='ledger'),
    path('recipe/1', recipes_1_view, name='recipe1'),
    path('recipe/2', recipes_2_view, name='recipe2')
]

app_name = 'ledger'