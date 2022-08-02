from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_lenght=20)
    quantity = models.IntegerField(max_lenght=4)
    price = models.IntegerField(max_lenght=4)

    def __str__(self):
        return self.name + " | " + " Cantidad disponible:" + self.quantity + " Precio: " + self.price

class menuItem(models.Model):
    name = models.CharField(max_lenght=20)
    price = models.IntegerField(max_lenght=4)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " | " + " Ingredientes usados: " + self.ingredient + " Precio: " + self.price

class purchased (models.Model):
    hour = models.DateTimeField()
    menuItem = models.ForeignKey(menuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hour + " | " + " Plato comprado: " + self.menuItem + " Ingredientes usados: " + self.ingredient
