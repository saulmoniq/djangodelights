from django.db.models import F
from codecs import charmap_build
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
        return self.name + " | " + " Qty available: " + str(self.quantity) + " Price/unit: " + str(self.price) + " Unit: " + self.unit

class menuItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name + " Price: " + str(self.price)


class RecipeRequirement(models.Model):
    quantity = models.FloatField(default=0)
    menuItem = models.ForeignKey(menuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,  blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menuItem) + " | " + " Quantity " + str(self.quantity) +" Ingredient: " + str(self.ingredient)

    # def __purchase__(self):
    #     if self.quantity <= self.Ingredient.quantity:
    #         Revisar esto, para poder modificar la BD de Ingredientes.
    #          Ingredient.objects.filter(pk=self.ingredient_id).update(quantity=F('quantity')+1)
    #          Ingredient.save()
    #             Movie.objects.filter(pk=self.movie_id).update( stock=F('stock')+1)
    #             https://docs.djangoproject.com/en/4.1/ref/models/expressions/
    #     else:
    #          self.ingredient.quantity += self.quantity
             

class purchased (models.Model):
    hour = models.DateTimeField(default="")
    recipeRequirement = models.ForeignKey(RecipeRequirement, null=True, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return str(self.hour) + " | " + " Item acquired: " + str(self.recipeRequirement)
    #     return self.__purchase__()

