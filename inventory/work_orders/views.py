from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import job_form, required_form


# Create your views here.
def activity_list(request):
    tasks = jobs.objects.all()
    return render(request, 'activities.html', {'header': 'Activities',
                                               'tasks': tasks})


def job_information(request, jobid):
    task = get_object_or_404(jobs, jobid=jobid)
    required_instance = required.objects.all().filter(reqid=task.pk)
    if request.method == "POST":
        form = job_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = job_form(instance=task)
        return render(request, 'workinfo.html', {'jobForm': form,
                                                 'required': required_instance,
                                                 'jobid': task.jobid})


def add_required_part(request, jobid):
    task = get_object_or_404(jobs, jobid=jobid)
    required_instance = required.objects.all().filter(reqid=task.pk)
    if request.method == "POST":
        form = required_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = required_form()
        return render(request, 'addrequired.html', {'RequiredPartForm': form,
                                                    'required': required_instance,
                                                    'jobid': task.jobid})

# # use for getting all files in instruction model relating to job from jobs model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
