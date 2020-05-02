from django.urls import path
from .views import *

urlpatterns = [
    path('activities/', activity_list, name='activities'),  # URL path for inventory_list view
    path('<str:jobid>/', job_information, name='detail'),
    # path('inventory/new/', new_part, name='new'),
]
