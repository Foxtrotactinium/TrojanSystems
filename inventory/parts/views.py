from django.shortcuts import render
from .models import *

# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return render(request, 'inventory.html', context)