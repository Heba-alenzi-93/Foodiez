from django.shortcuts import render,redirect
from .models import Recipe,Category,Ingrediant
from .forms import RegisterForm
from django.contrib.auth import login



# Create your views here.
def get_Recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes":recipes}
    return render(request,"recipes.html",context)


def register_user(request):
    form =  RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(user.password)
            user.save()
            login(request,user)
            return redirect("recipes_list")
    context = {
        "form":form,
    }
    return render (request, "register.html",context)
