from django.contrib import admin
from .models import Category,Recipe,Ingrediant
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display =  ("recipe_name","created_by")
    list_filter = ("created_by",)

admin.site.register(Category)
admin.site.register(Ingrediant)
admin.site.register(Recipe,RecipeAdmin)

