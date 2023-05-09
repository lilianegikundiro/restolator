from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import *


urlpatterns = [
	path('', RedirectView.as_view(url=reverse_lazy('registration')), name='start_page'),
	path('inventory', InventoryView.as_view(), name='inventory'),
	path('inventory/add', IngredientCreateView.as_view(), name='create_ingredient'),
	path('inventory/<pk>', IngredientUpdateView.as_view(), name='update_ingredient'),
	path('inventory/<pk>/delete', IngredientDeleteView.as_view(), name='delete_ingredient'),
	path('menu', MenuView.as_view(), name='menu'),
    path('reciperequirement', RecipeRequirementView.as_view(), name='reciperequirement'),
    path('reciperequirement/add', RecipeRequirementCreateView.as_view(), name='create_reciperequirement'),
	path('registration', RegisterUser.as_view(), name='registration'),
	path('login', LoginUser.as_view(), name='login'),
	path('logout', LogoutUser, name='logout'),
    path('menu/add', MenuCreateView.as_view(), name='create_menu'),
    path('menu/<pk>', MenuUpdateView.as_view(), name='update_menu'),
    path('menu/<pk>/delete', MenuDeleteView.as_view(), name='delete_menu'),
    path("purchase/", PurchaseView.as_view(), name="purchaselist"),
    path("purchase/create/", PurchaseCreateView.as_view(), name="purchasecreate"),
    path("report/", ReportView.as_view(), name="report"),
]

handler404 = pageNotFound