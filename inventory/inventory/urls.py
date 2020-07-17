"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from parts.views import register, logout_request, login_request, supplier_list, supplier_information
from work_orders.views import tasks, add_task, work_centre_list, add_work, task_information

urlpatterns = [
    path('admin/', admin.site.urls),
    path("suppliers/", supplier_list, name="suppliers"),
    path('suppliers/<str:id>/', supplier_information, name='supplier_information'),
    path('inventory/', include('parts.urls')),  # includes URLS's from parts app for hygiene
    path('activities/', include('work_orders.urls')),
    path("register/", register, name="register.html"),
    path("logout/", logout_request, name="logout"),
    path("login/", login_request, name="login"),
    path('tasks/', tasks, name='tasks'),
    path('tasks/addtask/', add_task, name='addtask'),
    path('tasks/<str:id>/', task_information, name='taskinformation'),
    path('workcentre/', work_centre_list, name='workcentre'),
    path('workcentre/addworkcentre/', add_work, name='addwork')
]
