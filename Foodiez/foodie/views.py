from django.shortcuts import render,redirect
from .models import Recipe,Category,Ingrediant
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate



# Create your views here.
def get_Recipes(request):
    recipes = Recipe.objects.all()
    context = {"recipes":recipes}
    return render(request,"recipes.html",context)

# Register View 
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



# Login View 
def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("recipes_list")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

