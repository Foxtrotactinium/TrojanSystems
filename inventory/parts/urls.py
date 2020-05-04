from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/', inventory_list, name='inventory'),  # URL path for inventory_list view
    path('inventory/<str:partnumber>/', part_information, name='detail'),
    path('inventory/new/', new_part, name='new'),
    path('', index, name='index'),
]
