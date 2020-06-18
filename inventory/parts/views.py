from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import part_form, supplier_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    partsuppliers_list = partsuppliers.objects.all()

    for part in parts:
        allsuppliers = partsuppliers_list.filter(partnumber=part.id)
        if allsuppliers.count() > 1:
            part.supplier = allsuppliers.get_object_or_404(preferrd=True)

        else:
            part.supplier = allsuppliers.first()

    template = loader.get_template('inventory.html')
    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return HttpResponse(template.render(context, request))


def part_information(request, id):
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


def register(request):
    if request.method == "POST":
        login_form = UserCreationForm(request.POST)
        if login_form.is_valid():
            user = login_form.save()
            username = login_form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("inventory:inventory")

        else:
            for msg in login_form.error_messages:
                messages.error(request, f"{msg}: {login_form.error_messages[msg]}")

            return render(request=request,
                          template_name="register.html",
                          context={"login_form": login_form})

            login_form = UserCreationForm
        return render(request=request,
                      template_name="register.html",
                      context={"login_form": login_form})
    else:
        login_form = UserCreationForm
        return render(request=request,
                      template_name="register.html",
                      context={"login_form": login_form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("inventory")


def login_request(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('inventory')

            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    login_form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"login_form": login_form})
