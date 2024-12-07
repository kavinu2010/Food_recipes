from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    # path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
