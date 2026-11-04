from django.urls import path

from recipes.views import home, contato, sobre

# dominio/recipes/home ou outros, sobre, contatos 
urlpatterns = [
    path('', home), #Home
    path('sobre/', sobre), #/sobre/ 
    path('contato/',  contato), # /contato/ 
]

# parei na 20