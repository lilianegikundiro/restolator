from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import *


urlpatterns = [
	path('', RedirectView.as_view(url=reverse_lazy('menu')), name='start_page'),
	path('inventory', InventoryView.as_view(), name='inventory'),
	path('inventory/add', IngredientCreateView.as_view(), name='create_ingredient'),
	path('inventory/<pk>', IngredientUpdateView.as_view(), name='update_ingredient'),
	path('inventory/<pk>/delete', IngredientDeleteView.as_view(), name='delete_ingredient'),
	path('menu', MenuView.as_view(), name='menu'),
    path('reciperequirement', RecipeRequirementView.as_view(), name='reciperequirement'),
     path('reciperequirement/add', RecipeRequirementCreateView.as_view(), name='create_reciperequirement'),
	# path('purchases', PurchaseView.as_view(), name='purchase'),
	# path('purchases/add', PurchaseCreateView.as_view(), name='create_purchase'),
	# path('purchases/<pk>/delete', PurchaseDeleteView.as_view(), name='delete_purchase'),
	# path('bookkeeping', FinanceView.as_view(), name='bookkeeping'),
	path('registration', RegisterUser.as_view(), name='registration'),
	path('login', LoginUser.as_view(), name='login'),
	path('logout', LogoutUser, name='logout'),
 
    path('menu/add', MenuCreateView.as_view(), name='create_menu'),
    path('menu/update', MenuUpdateView.as_view(), name='update_menu'),
    path('menu/delete', MenuDeleteView.as_view(), name='delete_menu'),
]

handler404 = pageNotFound