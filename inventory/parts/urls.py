from django.urls import path
from .views import *

urlpatterns = [
    path('', inventory_list, name='inventory'),  # URL path for inventory_list view
    path('<str:id>/', part_information, name='detail'),
    path('new/', new_part, name='new'),
    # path('', index, name='index'),
]
