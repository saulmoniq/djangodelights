from http.client import HTTPResponse
from traceback import format_exception_only
from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ingredient, RecipeRequirement, menuItem, purchased
from .forms import ingredientsCreateForm, menuItemCreateForm, purchasedCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    # Add your code below:
    
    user = authenticate(request, username=username, password=password)

    if user is not None:
      return redirect("home")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "inventory/login.html", context)

def logout_request(request):
  logout(request)
  return redirect("home")



class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "inventory/signup.html"

@login_required
def home(request):
    return render(request, 'home.html')

class IngredientView(ListView):
  model = Ingredient
  template_name = "inventory/ingredients_list.html"

class createIngredient(LoginRequiredMixin, CreateView):
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

