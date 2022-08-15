from django.contrib import admin
from foodie import models
# Register your models here.

@admin.register(models.Recipe)
class ReciepeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

