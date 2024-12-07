from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

# Home View (List of Recipes)
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

# Add Recipe View
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

# Recipe Detail View
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def delete_post(request, post_id):
    print(f"Attempting to delete post with ID: {post_id}")
    post = get_object_or_404(Recipe, id=post_id)
    print(f"Found post: {post}")
    post.delete()
    print("Post deleted successfully.")
    return redirect('home')