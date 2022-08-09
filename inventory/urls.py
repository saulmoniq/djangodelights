from django.urls import path

from . import views

urlpatterns = [
    path ('', views.home, name="home"),
    path ("create", views.createMenuItem.as_view(), name="createMenuItem")
]