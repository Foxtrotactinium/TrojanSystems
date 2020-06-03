from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import part_form


# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    partsuppliers_list = partsuppliers.objects.all()
    for part in parts:
        allsuppliers = partsuppliers_list.filter(partnumber=part.id)
        if( allsuppliers.count() > 1 ):
            part.supplier = allsuppliers.get_object_or_404(preferrd=True)
        else:
            part.supplier = allsuppliers.first()
        # part.supplier = part.supplier.partsupplier
    template = loader.get_template('inventory.html')
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return HttpResponse(template.render(context, request))


def part_information(request, id):
    part = get_object_or_404(partslist, id=id)
    # allparts = partslist.objects.all()
    # part = allparts.filter(pk=id)
    # print(part)
    # supplier_list = partsuppliers.objects.all()
    # part.supplier = supplier_list.filter(partnumber=part[0])
    # print(part.supplier)
    # print(part)
    if request.method == "POST":
        form = part_form(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = part_form(instance=part)
        print(form)
        print(part_form)
        print(part)
        # print(form, ' attributes of part object ')
        return render(request, 'detail.html', {'partForm': form})


def new_part(request):
    if request.method == "POST":
        form = part_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = part_form()
        print(form)
        return render(request, 'new.html', {'form': form})


def index(request):
    parts = partslist.objects.all()
    template = loader.get_template('index.html')
    context = {
        'parts': parts,
    }
    return HttpResponse(template.render(context, request))
