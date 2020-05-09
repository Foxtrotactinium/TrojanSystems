from django.urls import path
from work_orders.views import *

urlpatterns = [
    path('', activity_list, name='activities'),  # URL path for inventory_list view
    path('<str:jobid>/', job_information, name='workinfo'),
    # path('inventory/new/', new_part, name='new'),
]
