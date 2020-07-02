from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import part_form, supplier_form, part_comment_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def inventory_list(request):
    parts = partslist.objects.all()
    for part in parts:
        allsuppliers = partsuppliers.objects.all().filter(partnumber=part.id)
        if allsuppliers.count() > 1:
            part.supplier = allsuppliers.get_object_or_404(preferred=True)

        else:
            part.supplier = allsuppliers.first()

    context = {
        'parts': parts,
        'header': 'Inventory'
    }
    return render(request, 'inventory.html', context)

def supplier_list(request):
    partsuppliers = suppliers.objects.all()

    context = {
        'header': 'Supplier List',
        'partsuppliers': partsuppliers,
    }
    return render(request, 'suppliers.html', context)

def part_information(request, id):
    part = partslist.objects.all().filter(pk=id).first()
    part_suppliers = partsuppliers.objects.all().filter(partnumber=part)
    part_comments = partComments.objects.all().filter(commentedpart=part)

    if request.method == "POST":
        if 'save' in request.POST:
            form = part_form(request.POST, instance=part)
            if form.is_valid():
                form.save()
                return redirect('inventory')

        elif 'addcomment' in request.POST:
            form = part_comment_form(request.POST, instance=part_comments)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('inventory')

    else:
        form1 = part_form(instance=part)
        form2 = part_comment_form(request.POST, instance=part)
        return render(request, 'detail.html', {'partForm': form1,
                                               'commentForm': form2,
                                               'suppliers': part_suppliers,
                                               'comments': part_comments})

def supplier_information(request, id):
    partsupplier = suppliers.objects.all().filter(pk=id).first()
    supplierparts = partsuppliers.objects.all().filter(partsupplier=id)

    if request.method == "POST":
        form = supplier_form(request.POST, instance=partsupplier)
        if form.is_valid():
            form.save()
            return redirect('suppliers')

    else:
        form = supplier_form(instance=partsupplier)
        return render(request, 'supplier.html', {'supplierForm': form,
                                                 'supplierparts': supplierparts})

def add_supplier(request):
    if request.method == "POST":
        form = supplier_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('detail')

    else:
        form = supplier_form()
        return render(request, 'supplier.html', {'SupplierForm': form})


def new_part(request):
    if request.method == "POST":
        form = part_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = part_form()
        return render(request, 'new.html', {'PartForm': form})


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
