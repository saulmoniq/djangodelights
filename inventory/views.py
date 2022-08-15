from traceback import format_exception_only
from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ingredient, menuItem, purchased
from .forms import ingredientsCreateForm, menuItemCreateForm, purchasedCreateForm
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
  success_url = "http://127.0.0.1:8000/"
  template_name = "inventory/delete_ingredient.html"

class updateIngredient(UpdateView):
  model = Ingredient
  form_class = ingredientsCreateForm
  template_name = "inventory/update_ingredient.html"


class menuItemView(ListView):
  model = menuItem
  template_name = "inventory/menuItem_list.html"

class createMenuItem(CreateView):
  model = menuItem
  form_class = menuItemCreateForm
  template_name = "inventory/menuItem_create_form.html"

class deleteMenuItem(DeleteView):
  model = menuItem
  success_url = "/menuitems-list"
  template_name = "inventory/delete_menuitem.html"

class updatemenuItem(UpdateView):
  model = menuItem
  form_class = menuItemCreateForm
  template_name = "inventory/update_menuitem.html"

class listPurchase(ListView):
  model = purchased
  template_name = "inventory/list_purchased.html"

class createPurchased(CreateView):
  model = purchased
  form_class = purchasedCreateForm
  template_name = "inventory/purchased_create_form.html"

class updatePurchased(UpdateView):
  model = purchased
  form_class = purchasedCreateForm
  template_name = "inventory/update_purchased.html"

class deletePurchased(DeleteView):
  model = purchased
  success_url = "/listpurchased"
  template_name = "inventory/delete_purchased.html"