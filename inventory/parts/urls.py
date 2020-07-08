from django.urls import path
from .views import *

urlpatterns = [
    path('', inventory_list, name='inventory'),  # URL path for inventory_list view
    path('new/', new_part, name='new'),
    path('<str:id>/', part_information, name='detail'),
    path('addsupplier', add_supplier, name='addsupplier'),
    # path('<str:id>/addsupplier', add_supplier, name='supplier'),
]
