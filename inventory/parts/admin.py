from django.contrib import admin
from work_orders.models import *
from .models import PartsList, Suppliers, PartSuppliers, PartComments
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class partsresource(resources.ModelResource):

    class Meta:
        model = PartsList

class supplierresource(resources.ModelResource):

    class Meta:
        model = Suppliers

class partsupplierresource(resources.ModelResource):

    class Meta:
        model = PartSuppliers

class partcommentsresource(resources.ModelResource):

    class Meta:
        model = PartComments


# class partcommentsdmin(admin.ModelAdmin):
#     list_display = ('timestamp', 'author', 'part', 'comments')
#     readonly_fields = ('timestamp',)

class importparts(ImportExportModelAdmin):
    resource_class = partsresource

class jobsresource(resources.ModelResource):

    class Meta:
        model = Jobs

admin.site.register(PartsList, importparts)
admin.site.register(Jobs)
admin.site.register(Suppliers)
admin.site.register(PartSuppliers)
admin.site.register(Required)
admin.site.register(PartComments)
admin.site.register(ActivityLog)