from tkinter import CASCADE
from django.db import models
import datetime
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    unit = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name + " | " + " Cantidad disponible:" + str(self.quantity) + " Precio: " + str(self.price)

class menuItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name + " | " + " Ingredientes usados: " + " Precio: " + str(self.price)


class purchased (models.Model):
    hour = models.DateTimeField(default="")
    menuItem = models.ForeignKey(menuItem, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.hour) + " | " + " Plato comprado: " +" Ingredientes usados: "


class RecipeRequirement(models.Model):
    quantity = models.FloatField(default=0)
    menuItem = models.ForeignKey(menuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,  blank=True, on_delete=models.CASCADE)
