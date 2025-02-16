from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes_view, name='ledger'),
    #path('', views.recipes_1_view, name='ledger'),
    #path('', views.recipes_2_view, name='ledger')
]

app_name = 'ledger'