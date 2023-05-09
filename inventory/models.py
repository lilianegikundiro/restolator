
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Ingredient(models.Model):
   ingredient_name = models.CharField(max_length=60, unique=True)
   quantity = models.DecimalField(max_digits=12, decimal_places=6, default=0)
   class PossibleUnits(models.TextChoices):
       GRAM = 'g.', _('grams')
       KILO = 'kg.', _('kilos')
       LITER = 'L.', _('liters')
       MLITER = 'ml.', _('milliliters')
       AMOUNT = 'num', _('amount')
   units = models.CharField(max_length=3, choices=PossibleUnits.choices, default=PossibleUnits.AMOUNT)
   unit_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
   def __str__(self):
       return self.ingredient_name


class MenuItem(models.Model):
   recipe = models.CharField(max_length=255, unique=True)
   ingredients=models.ManyToManyField(Ingredient, through="RecipeRequirement")
   price = models.DecimalField(max_digits=5, decimal_places=2,default=0, )
   
   def __str__(self):
        return self.recipe
    
   def available(self):
        return all(i.enough() for i in RecipeRequirement.objects.filter(menu_item=self.id))

   def __str__(self):
        return f"{self.recipe}"
   

class RecipeRequirement(models.Model):
   menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,related_name='menuitem')
   ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE,related_name="ingredient")
   quantity_required = models.DecimalField(max_digits=12, decimal_places=6, default=0)
   
   def get_absolute_url(self):
        return "/menu"
    
   def enough(self):
        return self.quantity_required <= self.ingredient.quantity


   def __str__(self):
       return 'For {}: {} {} {}'.format(self.menu_item.recipe, self.quantity_required, self.ingredient.units, self.ingredient.ingredient_name)
   
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchase"

    def revenue(self):
        return self.menu_item.price

    def cost(self):
        total = 0
        reqs = RecipeRequirement.objects.filter(menu_item=self.menu_item.id)
        for req in reqs:
            price = req.quantity_required * req.ingredient.unit_price
            total += price
        return total

    def profit(self):
        return self.revenue() - self.cost()

    def __str__(self):
        return f"Recipe:{self.menu_item.recipe}; Time:{self.timestamp}"

    












