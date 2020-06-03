from django.contrib import admin
from work_orders.models import *
from .models import partslist, suppliers, partsuppliers
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class partsresource(resources.ModelResource):

    class Meta:
        model = partslist

class supplierresource(resources.ModelResource):

    class Meta:
        model = suppliers

class partsupplierresource(resources.ModelResource):

    class Meta:
        model = partsuppliers

class importparts(ImportExportModelAdmin):
    resource_class = partsresource

class jobsresource(resources.ModelResource):

    class Meta:
        model = jobs

admin.site.register(partslist, importparts)
admin.site.register(jobs)
admin.site.register(suppliers)
admin.site.register(partsuppliers)