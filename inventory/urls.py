from django.urls import path

from . import views

urlpatterns = [
    path ('', views.home, name="home"),
    path('login', views.login_view, name="login"),
    path ("create", views.createMenuItem.as_view(), name="createMenuItem"),
    path("ingredients-list", views.IngredientView.as_view(), name="ingredients"),
    path("add-ingredient", views.createIngredient.as_view(), name="ingredientsCreateForm"),
    path('menuitems-list', views.menuItemView.as_view(), name="menuItemView"),
    path('<pk>/delete', views.deleteIngredient.as_view(), name="deleteIngredient"),
    path('<pk>/update', views.updateIngredient.as_view(), name="updateIngredient"),
    path('<pk>/deletemenuitem', views.deleteMenuItem.as_view(), name="deleteMenuItem"),
    path('<pk>/updatemenuitem', views.updatemenuItem.as_view(), name="updateMenuItem"),
    path('listpurchased', views.listPurchase.as_view(), name="listPurchased"),
    path('createpurchased', views.createPurchased.as_view(), name = "createPurchased"),
    path('<pk>/updatepurchased', views.updatePurchased.as_view(), name="updatePurchased"),
    path('<pk>/deletepurchased', views.deletePurchased.as_view(), name="purchased_delete"),
]