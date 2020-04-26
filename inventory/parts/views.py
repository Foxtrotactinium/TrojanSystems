from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import *


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


# def part_information(request):
#     rid = request.path[1:len(request.path)-1]
#     part = partslist.objects.get(id=rid)
#     # part = request.POST.get('part')
#     print('value parsed ', request.data)
#     template = loader.get_template('detail.html')
#     context = {
#         'part': part,
#     }
#     return HttpResponse(template.render(context, request))


def part_information(request, partnumber): #, part_form
    part = get_object_or_404(partslist, partnumber=partnumber)
    print(part)

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
        print(form.as_ul())
        # print(form, ' attributes of part object ')
        return render(request, 'detail.html', {'form': form})


    # """This view returns part information to view and edit"""
    # print('value parsed ', partnumber)
    # """"Import chosen part in table row from partslist"""
    # part = get_object_or_404(partslist, partnumber=partnumber)
    # # print(part, ' AND ', HttpRequest.GET)
    # template = loader.get_template('detail.html')
    # context = {
    #     'part': part,
    # }
    # # render template with nodes
    # return HttpResponse(template.render(context, request))

def index(request):
    parts = partslist.objects.all()
    template = loader.get_template('index.html')
    context = {
        'parts': parts,
    }
    return HttpResponse(template.render(context, request))
