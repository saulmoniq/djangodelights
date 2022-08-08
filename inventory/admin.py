from django.contrib import admin
from inventory import models

# Register your models here.
admin.site.register(models.Ingredient)
admin.site.register(models.menuItem)
admin.site.register(models.purchased)
admin.site.register(models.RecipeRequirement)

# @admin.register(RecipeRequirement)
# class RecipeRequirement(admin.ModelAdmin):
#   list_display = [field.name for field in
# RecipeRequirement._meta.get_fields()]