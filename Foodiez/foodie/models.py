from django.db import models
from django.conf import settings

# Create your models here.

class Recipe (models.Model):
    recipe_name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category")
    ingredients =  models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipe"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="avtars/",null=True )

    def __str__(self):
        return self.recipe_name





class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name