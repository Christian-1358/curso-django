from django.urls import path

from recipes.views import home

# dominio/recipes/home ou outros, sobre, contatos 
urlpatterns = [
    path('', home), #Home

]


# parei na 20