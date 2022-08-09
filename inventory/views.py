from django.shortcuts import render

# Create your views here.
def home(request):
  # The context is all of the variables we want passed into the template.
    return render(request, 'inventory/home.html')