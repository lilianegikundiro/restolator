from typing import Any, Dict
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
 
	def get_context_data(self):
		context= super().get_context_data()
		context["menuitems"] = MenuItem.objects.all()
		context["reqs"] = RecipeRequirement.objects.all()
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
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
	def form_valid(self, form):	# login to account after registration
		user = form.save()
		login(self.request, user)
		return redirect('login')


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

class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()
        return context
class PurchaseCreateView(LoginRequiredMixin, TemplateView):
    model = Purchase
    template_name = "inventory/purchase_create.html"
    form_class = PurchaseForm

    def get_context_data(self):
        context = super().get_context_data()
        context["menu_items"] = [item for item in MenuItem.objects.all() if item.available()]
        return context

    def post(self, request):
        menu_item_title = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(recipe=menu_item_title)
        reqs = RecipeRequirement.objects.filter(menu_item=menu_item)
        purchase = Purchase(menu_item=menu_item)
        # Update ingredient quantity in inventory
        for req in reqs:
            req.ingredient.quantity -= req.quantity_required
            req.ingredient.save()
        purchase.save()
        return redirect("/purchase")
    

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/report.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()
        context["revenues"] = [purchase.revenue() for purchase in Purchase.objects.all()]
        context["costs"] = [purchase.cost() for purchase in Purchase.objects.all()]
        context["profit"] = sum([purchase.profit() for purchase in Purchase.objects.all()])
        return context
