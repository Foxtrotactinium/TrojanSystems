from django.db import models
# from django.contrib.postgres.fields import ArrayField
from parts.models import partslist


# Create your models here.
class jobs(models.Model):
    jobid = models.CharField(max_length=100)
    partsrequired = models.ManyToManyField(partslist, related_name='required_for_jobs')
    partsproduced = models.ManyToManyField(partslist, related_name='produced_for_jobs')


# class instruction(models.Model):
#     job = models.ForeignKey(jobs)
#     pdf = models.FileField(upload_to='pdf')
