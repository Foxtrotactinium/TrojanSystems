from django.db import models
# from django.contrib.postgres.fields import ArrayField
from parts.models import PartsList
from django.contrib.auth.models import User


# Create your models here.
class Jobs(models.Model):
    jobid = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.jobid


class Required(models.Model):
    reqid = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    partsrequired = models.ForeignKey(PartsList, related_name='required_for_jobs', on_delete=models.CASCADE)
    quantityrequired = models.IntegerField(default=1)
    increment = models.BooleanField(default=False)     # TRUE/FALSE used to represent parts Required/produced

    def __str__(self):
        return str(self.reqid)+" "+str(self.partsrequired)


class ActivityLog(models.Model):
    activity_name = models.CharField(max_length=50)
    jobid = models.ForeignKey(Jobs, on_delete=models.PROTECT)
    partsrequired = models.ForeignKey(PartsList, on_delete=models.PROTECT)
    increment = models.BooleanField(default=False)
    quantityrequired = models.IntegerField()
    quantitycompleted = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.supplier
# class instruction(models.Model):
#     job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
#     pdf = models.FileField(upload_to='pdf')
