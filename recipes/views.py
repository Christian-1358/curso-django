
from django.shortcuts import render
from recipes.utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [
            {**make_recipe(), 'id': recipe_id}
            for recipe_id in range(1, 11)
        ],
    })

# aonde vai as "urls" e tals

def recipe(request, id):
    recipe = {**make_recipe(), 'id': id}
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        
    })
