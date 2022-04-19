from django.shortcuts import render, redirect

# Create your views here.
from recipes.web.forms import CreateRecipeForm, DeleteRecipeForm
from recipes.web.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


    #TODO implement ingridient separation
def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm(instance=recipe)

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteRecipeForm(instance=recipe)


    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    recipe_ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': recipe_ingredients,
    }


    return render(request, 'details.html', context)
