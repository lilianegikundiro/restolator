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
    class Meta:
        model = MenuItem
        fields = "__all__"
  
class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
  
class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
 
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
	
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['menu_item',]