from django.urls import path
from .views import *

urlpatterns = [
    path('', inventory_list, name='inventory'),  # URL path for inventory_list view
    path('addpart/', add_part, name='addpart'),
    path('<str:id>/', part_information, name='detail'),
    path('addsupplier', add_supplier, name='addsupplier'),
]
