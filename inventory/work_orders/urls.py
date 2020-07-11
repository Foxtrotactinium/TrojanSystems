from django.urls import path
from work_orders.views import activity_list, job_information, add_required_part, add_activity, tasks

urlpatterns = [
    path('', activity_list, name='activities'),  # URL path for inventory_list view
    path('addactivity/', add_activity, name='addactivity'),
    path('<str:id>/', job_information, name='workinfo'),
    path('<str:id>/addrequired', add_required_part, name='addrequired'),
]
