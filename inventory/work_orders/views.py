from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import job_form, required_form


# Create your views here.
def activity_list(request):
    return render(request, 'activities.html', {'header': 'Activities',
                                               'tasks': Jobs.objects.all()})


def add_activity(request):
    if request.method == "POST":
        form = job_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = job_form()

        return render(request, 'addactivity.html', {'jobform': form})


def job_information(request, jobid):
    task = get_object_or_404(Jobs, jobid=jobid)
    if request.method == "POST":
        form = job_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = job_form(instance=task)
        return render(request, 'workinfo.html', {'jobform': form,
                                                 'required': Required.objects.all().filter(reqid=task.pk),
                                                 'jobid': task.jobid})


def add_required_part(request, jobid):
    task = get_object_or_404(Jobs, jobid=jobid)
    required_instance = Required.objects.all().filter(reqid=task.pk)
    parts = PartsList.objects.all()
    if request.method == "POST":
        form = required_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = required_form(initial={'reqid': jobid})
        print(jobid)
        return render(request, 'addrequired.html', {'requiredpartform': form,
                                                    'required': required_instance,
                                                    'parts': parts,
                                                    })

# # use for getting all files in instruction model relating to job from Jobs model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
