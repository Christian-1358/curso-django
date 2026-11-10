from django.urls import path

from . import views
# dominio/recipes/home ou outros, sobre, contatos 
urlpatterns = [
    path('', views.home), #Home
    path('recipes/<int:id>/', views.recipe),
]


# parei na 20