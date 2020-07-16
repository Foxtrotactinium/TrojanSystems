from django.db import models
# from django.contrib.postgres.fields import ArrayField
from parts.models import PartsList
from django.contrib.auth.models import User


# Create your models here.
class Activities(models.Model):
    activityid = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.activityid)


class ActivityRequiredParts(models.Model):
    activityid = models.ForeignKey(Activities, on_delete=models.CASCADE)
    partsrequired = models.ForeignKey(PartsList, related_name='required_for_jobs', on_delete=models.CASCADE)
    quantityrequired = models.IntegerField(default=1)
    increment = models.BooleanField(default=False)     # TRUE/FALSE used to represent parts ActivityRequiredParts/produced

    def __str__(self):
        return str(self.activityid) + " " + str(self.partsrequired)


class Tasks(models.Model):
    task_name = models.CharField(max_length=50)
    activityid = models.ForeignKey(Activities, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.task_name) + ' ' + str(self.activityid)


class WorkCentre(models.Model):
    vehicle = models.CharField(max_length=50)
    task_name = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    activityid = models.ForeignKey(Activities, on_delete=models.PROTECT)
    partsrequired = models.ForeignKey(PartsList, on_delete=models.PROTECT)
    increment = models.BooleanField(default=False)
    quantityrequired = models.IntegerField()
    quantitycompleted = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    complete = models.BooleanField(default=False)
    notes = models.TextField()


# class instruction(models.Model):
#     job = models.ForeignKey(Activities, on_delete=models.CASCADE)
#     pdf = models.FileField(upload_to='pdf')
