
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



###########################################################################

"""
[1]
"""

# category class [name,desctription,cerated_by]
class Category(models.Model): 
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(default="")
    created_by = models.ForeignKey(
       User, on_delete=models.CASCADE, related_name="category",null=True)
    def __str__(self):
        return self.name


###########################################################################

"""
[2]
"""


# Ingrediant class [name,image,category_name]
class Ingrediant(models.Model):
    name = models.CharField(unique=True, max_length=100)
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="ingredient",)
    image = models.ImageField(upload_to="avtars/")
    

    def __str__(self):
        return self.name





###########################################################################

"""
[3]
"""

# Recipe class [recipe_name,ingredients, created_by, created_at, image ]
class Recipe (models.Model):
    recipe_name = models.CharField(unique=True,max_length=100)
    category_name = models.ManyToManyField(Category, related_name="categories" )
    ingredients = models.ManyToManyField(Ingrediant, related_name="ingredients" )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipe")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="avtars/",null=True )
    description = models.TextField(null=True) 

    def __str__(self):
        return self.recipe_name









