from django.db import models
# from django.contrib.postgres.fields import ArrayField
from parts.models import partslist


# Create your models here.
class jobs(models.Model):
    jobid = models.CharField(max_length=100)

    def __str__(self):
        return self.jobid

class required(models.Model):
    reqid = models.ForeignKey(jobs, on_delete=models.CASCADE)
    partsrequired = models.ForeignKey(partslist, related_name='required_for_jobs', on_delete=models.CASCADE)
    quantityrequired = models.IntegerField(default=1)

class produced(models.Model):
    prodid = models.ForeignKey(jobs, on_delete=models.CASCADE)
    partsproduced = models.ManyToManyField(partslist, related_name='produced_for_jobs')
    quantityproduced = models.IntegerField(default=1)

# class instruction(models.Model):
#     job = models.ForeignKey(jobs, on_delete=models.CASCADE)
#     pdf = models.FileField(upload_to='pdf')
