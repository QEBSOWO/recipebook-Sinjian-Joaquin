from django.urls import path, include



from .views import recipe_list_view, recipe_detail_view, recipe_add_view, recipe_update_view

urlpatterns = [
    path('recipes/list', recipe_list_view, name='recipe_list'),
    path('recipe/<int:pk>', recipe_detail_view, name='recipe_detail'),
    path('recipe/add', recipe_add_view, name='recipe_add'),
    path('recipe/<int:pk>/add_image', recipe_update_view, name='recipe_update')
]

app_name = 'ledger'