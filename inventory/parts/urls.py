from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/', inventory_list, name='inventory'), # URL path for inventory_list view
    ]