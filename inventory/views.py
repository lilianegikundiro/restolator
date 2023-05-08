from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class MenuView(ListView):
	model = MenuItem
	template_name = 'inventory/menu.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class MenuCreateView(LoginRequiredMixin, CreateView):
	model = MenuItem
	form_class = MenuForm
	template_name = 'inventory/create_menu.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class MenuUpdateView(LoginRequiredMixin,UpdateView):
	model = MenuItem
	form_class = MenuForm
	template_name = 'inventory/update_menu.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class MenuDeleteView(LoginRequiredMixin, DeleteView):
	model = MenuItem
	template_name = 'inventory/delete_confirm.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class InventoryView(LoginRequiredMixin, ListView):
	model = Ingredient
	template_name = 'inventory/inventory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class IngredientCreateView(LoginRequiredMixin, CreateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/create_ingredient.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class IngredientUpdateView(LoginRequiredMixin,UpdateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/update_ingredient.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
	model = Ingredient
	template_name = 'inventory/delete_confirm.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


# User functionality views:
class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = 'inventory/registration.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
	def form_valid(self, form):	# login to account after registration
		user = form.save()
		login(self.request, user)
		return redirect('menu')


class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'inventory/login.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
	def get_success_url(self) -> str:	# "redirect" in LoginView
		return reverse_lazy('menu')


def LogoutUser(request):
	logout(request)
	return redirect('login')

#Exceptions
def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>ERROR 404</h1><br><p>Page Not Found</p>')

class RecipeRequirementView(ListView):
	model = RecipeRequirement
	template_name = 'inventory/reciperequirement.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
	model = RecipeRequirement
	form_class = RecipeRequirementForm
	template_name = 'inventory/create_reciperequirement.html'
	success_url = reverse_lazy('reciperequirement')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context