from django.urls import path, include



from .views import recipe_list_view, recipe_detail_view, recipe_add_view

urlpatterns = [
    path('recipes/list', recipe_list_view, name='ledger'),
    path('recipe/<int:pk>', recipe_detail_view, name='recipe_detail'),
    path('recipe/add', recipe_add_view, name='recipe_add')
]

app_name = 'ledger'