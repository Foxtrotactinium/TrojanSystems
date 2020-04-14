from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return render(request, 'inventory.html', context)

def detail_view(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = cls(instance=item)

        return render(request, 'detail.html', {'form': form})