from django.urls import path

from . import views
# dominio/recipes/home ou outros, sobre, contatos 
#recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), #Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]


# parei na 20