from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ingredient, menuItem
from .forms import ingredientsCreateForm, menuItemCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')

class IngredientView(ListView):
  model = Ingredient
  template_name = "inventory/ingredients_list.html"

class createIngredient(CreateView):
  model = Ingredient
  form_class = ingredientsCreateForm
  template_name = "inventory/ingredients_create_form.html"

class deleteIngredient(DeleteView):
  model = Ingredient
  success_url = reverse_lazy("")
  template_name = "inventory/delete_ingredient.html"

class menuItemView(ListView):
  model = menuItem
  template_name = "inventory/menuItem_list.html"

class createMenuItem(CreateView):
  model = menuItem
  form_class = menuItemCreateForm
  template_name = "inventory/menuItem_create_form.html"
