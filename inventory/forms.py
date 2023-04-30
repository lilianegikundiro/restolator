from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class IngredientForm(forms.ModelForm):
	ingredient_name = forms.CharField(label='Ingredient', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	quantity = forms.IntegerField(label='Quantity at the warehouse', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	unit_price = forms.CharField(label='Price per unit', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = Ingredient
		fields = '__all__'
  
class MenuForm(forms.ModelForm):
	recipe = forms.CharField(label='Menu Item', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	price = forms.CharField(label='Selling Price', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = MenuItem
		fields = '__all__'
# class MenuForm(forms.ModelForm):
# 	menu_item = forms.CharField(label='Menu Item', widget=forms.TextInput(attrs={'class': 'uk-input'}))
# 	ingredient =forms.CharField(label='Ingredients', widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
# 	class Meta:
# 		model = RecipeRequirement
# 		fields = '__all__'
  
class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
  
class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
 
# class PurchaseForm(forms.ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		super(PurchaseForm, self).__init__(*args, **kwargs)
# 		for dish in RecipeRequirement.objects.all():	# adds an input int for each position in menu to generate JSON later
# 			self.fields['{}'.format(dish.id)] = forms.IntegerField(label=dish.title, widget=forms.TextInput(attrs={'class': 'uk-input', 'value': 0}))
	
# 	def clean(self):
# 		'''Additionally generate JSON for menu_items field, checks valid of input for this field (is purchase not empty or is there enough ingredients on stock)'''
# 		cleaned_data = super(PurchaseForm, self).clean()
# 		menu_items = {}
# 		for dish in RecipeRequirement.objects.all():
# 			if cleaned_data.get('{}'.format(dish.id)) != 0:
# 				menu_items[dish.menu_item] = cleaned_data.get('{}'.format(dish.id))	# generating JSON from input of form

# 				for recipe in dish.menu_item.all():	# recipe is related_name of RecipeRequirement
# 					if (menu_items.ingredient.quantity - menu_items.require * menu_items[dish.title]) < 0:
# 						raise forms.ValidationError('Stock is too low. Not enough of: ' + str(recipe.ingredient))
# 		if not menu_items:
# 			raise forms.ValidationError('This purchase is empty')
# 		cleaned_data['menu_items'] = menu_items	# this would be saved to DB

# 	menu_items = forms.JSONField(required=False, widget=forms.HiddenInput())	# fake invisible field just to ModelForm methods save it to DB
# 	client = forms.ModelChoiceField(queryset=User.objects.all(), required=False, widget=forms.HiddenInput())
# 	class Meta:
# 		model = Purchase
# 		fields = '__all__'