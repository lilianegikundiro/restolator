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
	ingredients = forms.CharField(label='Ingredients', widget=forms.SelectMultiple(attrs={'class': 'uk-input'}))
	price = forms.CharField(label='Selling Price', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = MenuItem
		fields = ('recipe', 'ingredients','price')
# class MenuForm(forms.ModelForm):
# 	menu_item = forms.CharField(label='Menu Item', widget=forms.TextInput(attrs={'class': 'uk-input'}))
# 	ingredient =forms.CharField(label='Ingredients', widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
# 	class Meta:
# 		model = RecipeRequirement
# 		fields = '__all__'
  
class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
  
class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
 
class RecipeRequirementForm(forms.ModelForm):
	menu_item = forms.CharField(label='Menu Item', widget=forms.Select(attrs={'class': 'uk-input'}))
	ingredient = forms.CharField(label='Ingredient', widget=forms.SelectMultiple(attrs={'class': 'uk-input'}))
	quantity_required = forms.IntegerField(label="Required Ingredient",widget=forms.NumberInput(attrs={'class': 'uk-input'}))

	class Meta:
		model = RecipeRequirement
		fields = '__all__'
	