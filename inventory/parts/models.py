from django.db import models

# Inventory Model with fields
class partslist(models.Model):
    partnumber = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=20)
    supplier = models.CharField(max_length=50)
    stockonhand = models.IntegerField(blank=True)
    minimumstock = models.IntegerField(blank=True)
    reorderqtys = models.IntegerField(blank=True)
    qtyperassembly = models.IntegerField(blank=True)
    boxsize = models.IntegerField(blank=True)
    leadtime = models.CharField(max_length=50)
    weight = models.IntegerField(blank=True)

    # class Meta:
    #     abstract = True
# dunder used to return string value without conflicting with other variables
    def __str__(self):
        return 'Part : {0} Description {1} Location : {2} Supplier : {3} S.O.H : {4}'.format(self.partnumber, self.description, self.location, self.supplier, self.stockonhand)

