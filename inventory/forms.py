from django import forms

from .models import RecipeRequirement, menuItem, Ingredient, purchased

class menuItemCreateForm(forms.ModelForm):
    class Meta:
        model = menuItem
        fields = "__all__"

