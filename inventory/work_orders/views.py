from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import job_form, required_form, task_form


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


def job_information(request, id):
    task = get_object_or_404(Jobs, id=id)
    if request.method == "POST":
        form = job_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = job_form(instance=task)
        return render(request, 'workinfo.html', {'jobform': form,
                                                 'required': Required.objects.all().filter(reqid=task.pk),
                                                 'id': task.id})


def add_required_part(request, id):
    task = get_object_or_404(Jobs, id=id)
    required_instance = Required.objects.all().filter(reqid=task.pk)
    parts = PartsList.objects.all()
    if request.method == "POST":
        form = required_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = required_form(initial={'reqid': task.id})
        print(id)
        return render(request, 'addrequired.html', {'requiredpartform': form,
                                                    'required': required_instance,
                                                    'parts': parts,
                                                    })


def tasks(request):
    return render(request, 'tasks.html', {'header': 'Tasks',
                                          'tasks': ActivityLog.objects.all().filter(complete=False)})


def add_task(request):
    if request.method == "POST":
        form = task_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks')

    else:
        form = task_form()
        return render(request, 'addtask.html', {'taskform': form})

# # use for getting all files in instruction model relating to job from Jobs model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
