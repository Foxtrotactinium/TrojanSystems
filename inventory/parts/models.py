from django.db import models

# Inventory Model with fields
class partslist(models.Model):
    partnumber = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200,)
    location = models.CharField(max_length=20)
    supplier = models.CharField(max_length=50)
    stockonhand = models.IntegerField()
    minimumstock = models.IntegerField()
    reorderqtys = models.IntegerField()
    qtyperassembly = models.IntegerField()
    boxsize = models.IntegerField()
    leadtime = models.CharField(max_length=50)
    weight = models.IntegerField()

# dunder used to return string value without conflicting with other variables
    def __str__(self):
        return 'Part : {0} Description {1} Location : {2} Supplier : {3} S.O.H : {4}'.format(self.partnumber, self.description, self.location, self.supplier, self.stockonhand)