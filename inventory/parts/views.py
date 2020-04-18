from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    template = loader.get_template('inventory.html')
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return HttpResponse(template.render(context, request))


"""def detail_view(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    template = loader.get_template('detail.html')

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = cls(instance=item)

        return HttpResponse(template.render({'form': form}, request))
"""

def part_information(request, partnumber):
    """This view returns part information to view and edit"""

    selected_part = partslist.objects.get(partnumber)
    # user is posting: get edited node, change comment, and save
    """if request.POST:"""

    # render template with nodes
    return render(request, 'detail', {'selected_part': selected_part })

def index(request):
    parts = partslist.objects.all()
    template = loader.get_template('index.html')
    context = {
        'parts': parts,
    }
    return HttpResponse(template.render(context, request))
