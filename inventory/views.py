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




# class PurchaseView(LoginRequiredMixin, ListView):
# 	model = Purchase
# 	template_name = 'inventory/purchase.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
		

# 		return context


# class PurchaseCreateView(LoginRequiredMixin, CreateView):
# 	model = Purchase
# 	form_class = PurchaseForm
# 	template_name = 'inventory/create_purchase.html'
# 	success_url = reverse_lazy('purchase')

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['menu_items'] = MenuItem.objects.all()
		

# 		return context
	
# 	def form_valid(self, form):
# 		form.instance.client = self.request.user
# 		res = super().form_valid(form)
# 		form.instance.modify_inventory					# we already checked in PurchaseForm.clean() that we have enough ingredients, now we can modify their quantity after this purchase	
# 		form.save()

# 		return res

# class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
# 	model = Purchase
# 	template_name = 'inventory/delete_confirm.html'
# 	success_url = reverse_lazy('purchase')

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		mixin_context = self.get_user_context(title='Add Purchase', select=2)

# 		return dict(list(context.items()) + list(mixin_context.items()))

# class FinanceView(LoginRequiredMixin, TemplateView):
# 	template_name = 'inventory/bookkeeping.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		revenue = 0
# 		expenses = 0
# 		for p in Purchase.objects.all():
# 			expenses += p.total_expenses
# 			revenue += p.total_price
# 		context['total_revenue'] = revenue
# 		context['total_expenses'] = expenses
# 		context['total_profit'] = revenue - expenses
		

# 		return context
