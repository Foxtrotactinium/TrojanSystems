from django.db import models
from django.contrib.postgres.fields import ArrayField
from inventory.parts.models import partslist

# Create your models here.
class jobs(models.Model):
    jobid = models.CharField(max_length=100)
    partsrequired = ArrayField(
        ArrayField(
            models.ForeignKey(partslist, on_delete=models.CASCADE)
        )
    )
    partsproduced = ArrayField(
        ArrayField(
            models.ForeignKey(partslist, on_delete=models.CASCADE)
        )
    instruction =

    class Meta:
        processdescription = models.CharField()

