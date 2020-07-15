from django.urls import path
from work_orders.views import activity_list, activity_information, add_required_part_to_activity, add_activity, tasks

urlpatterns = [
    path('', activity_list, name='activities'),  # URL path for inventory_list view
    path('addactivity/', add_activity, name='addactivity'),
    path('<str:id>/', activity_information, name='activityinformation'),
    path('<str:id>/addrequired', add_required_part_to_activity, name='addrequired'),
]
