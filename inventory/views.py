from django.shortcuts import render
from .models import menuItem
from .forms import menuItemCreateForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')

class createMenuItem(CreateView):
  model = menuItem
  form_class = menuItemCreateForm
  template_name = "inventory/menuItem_create_form.html"
