from django.urls import path


from .views import recipe_list_view, recipe_detail_view

urlpatterns = [
    path('recipes/list', recipe_list_view.as_view(), name='ledger'),
    path('recipe/<int:pk>', recipe_detail_view.as_view(), name='recipe_detail'),
]

app_name = 'ledger'