from django.contrib import admin
from .models import partslist
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class partsresource(resources.ModelResource):

    class Meta:
        model = partslist

class importparts(ImportExportModelAdmin):
    resource_class = partsresource

admin.site.register(partslist, importparts)
