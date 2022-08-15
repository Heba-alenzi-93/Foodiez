from django.shortcuts import render
from .models import Recipe,Category,Ingrediant

# Create your views here.
def get_Recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes":recipes}
    return render(request,"recipes.html",context)
