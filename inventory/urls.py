from django.urls import path

from . import views

urlpatterns = [
    path ('', views.home, name="home"),
    path ("create", views.createMenuItem.as_view(), name="createMenuItem"),
    path("ingredients-list", views.IngredientView.as_view(), name="ingredients"),
    path("add-ingredient", views.createIngredient.as_view(), name="ingredientsCreateForm"),
    path('menuitems-list', views.menuItemView.as_view(), name="menuItemView"),
    path('<pk>/delete', views.deleteIngredient.as_view(), name="deleteIngredient"),
]