from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import part_form, supplier_form


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
    print(part)
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return HttpResponse(template.render(context, request))


def part_information(request, id):
    # part = get_object_or_404(partslist, id=id)
    allparts = partslist.objects.all()
    part = allparts.filter(pk=id).first()

    supplier_list = partsuppliers.objects.all()
    specific_suppliers = supplier_list.filter(partnumber=part)

    if request.method == "POST":
        form = part_form(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = part_form(instance=part)

        # print(form, ' attributes of part object ')
        return render(request, 'detail.html', {'partForm': form, 'suppliers': specific_suppliers})

def add_supplier(request):
    if request.method == "POST":
        form = supplier_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('detail')

    else:
        form = supplier_form()
        return render(request, 'supplier.html', {'form': form})


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
