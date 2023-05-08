
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
   

class RecipeRequirement(models.Model):
   menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,related_name='menuitem')
   ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE,related_name="ingredient")
   quantity_required = models.DecimalField(max_digits=12, decimal_places=6, default=0)
   def __str__(self):
       return 'For {}: {} {} {}'.format(self.menu_item.recipe, self.quantity_required, self.ingredient.units, self.ingredient.ingredient_name)
#    def ingredient_reduction(self, quantity):
#        if quantity <= 0:
#            message =  "Insufficient amount"
#            status = 403
#        elif quantity < self.quantity_required:
#             message = "You want to use more than you have"
#             status = 403
        
#        else:
#            self.quantity_required -= quantity
#            self.save()
#            message = f" you remain with {self.quantity}{self.ingredient_name}"
#            status = 200
#        return message,status    
    












