from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import activity_form, required_form, task_form, work_form
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def activity_list(request):
    return render(request, 'activities.html', {'header': 'Activities',
                                               'activities': Activities.objects.all()})


def add_activity(request):
    if request.method == "POST":
        form = activity_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = activity_form()

        return render(request, 'addactivity.html', {'activityform': form})


def activity_information(request, id):
    task = get_object_or_404(Activities, id=id)
    if request.method == "POST":
        form = activity_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = activity_form(instance=task)
        context = {'activityform': form,
                   'activitypartsrequired': ActivityRequiredParts.objects.all().filter(activityid=id),
                   'id': id}
        return render(request, 'activityinformation.html', context)


def add_required_part_to_activity(request, id):
    activity_parts = ActivityRequiredParts.objects.all().filter(activityid=id)
    parts = PartsList.objects.all()
    if request.method == "POST":
        form = required_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('activities')

    else:
        form = required_form(initial={'activityid': id})
        # form.fields['activityid'].disabled = True
        context = {'requiredpartform': form,
                   'activityrequiredparts': activity_parts,
                   'parts': parts,
                   }
    return render(request, 'addrequired.html', context)


def tasks(request):
    return render(request, 'tasks.html', {'header': 'Tasks',
                                          'tasks': Tasks.objects.all()})


def add_task(request):
    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            activity = form.cleaned_data['activityid']

            if Tasks.objects.all().filter(task_name=task_name).count() > 0:
                messages.error(request, "Task name exists")
                return redirect('addtask')

            required_list = ActivityRequiredParts.objects.all().filter(activityid=activity)
            for required in required_list:
                temp = Tasks(task_name=task_name,
                             activityid=activity,
                             # partsrequired=required.partsrequired,
                             # increment=required.increment,
                             # quantityrequired=required.quantityrequired,
                             # quantitycompleted=0,
                             # user=request.user,
                             complete=False,
                             )
                temp.save()
            return redirect('tasks')
    else:
        form = task_form()
        return render(request, 'addtask.html', {'taskform': form})


def work_centre_list(request):
    return render(request, 'workcentre.html', {'header': 'Outstanding Tasks',
                                               'workcentre': WorkCentre.objects.all().filter(complete=False)})


def add_work(request):
    if request.method == "POST":
        form = work_form(request.POST)
        if form.is_valid():
            vehicle = form.cleaned_data['vehicle']
            task_name = form.cleaned_data['task_name']
            print(task_name.task_name)
            notes = form.cleaned_data['notes']
            activity = get_object_or_404(Tasks, task_name=task_name.task_name.first())
            # activity = Tasks.objects.all().filter(task_name=task_name)
            print(activity)

            if WorkCentre.objects.all().filter(vehicle=vehicle).count() > 0:
                messages.error(request, "Vehicle already exists")
                return redirect('addwork')

            required_list = ActivityRequiredParts.objects.all().filter(activityid=activity)
            for required in required_list:
                temp = Tasks(vehicle=vehicle,
                             task_name=task_name,
                             activityid=activity.activityid,
                             partsrequired=required.partsrequired,
                             increment=required.increment,
                             quantityrequired=required.quantityrequired,
                             quantitycompleted=0,
                             timestamp=timezone.now(),
                             user=request.user,
                             complete=False,
                             notes=notes
                             )
                temp.save()
            return redirect('tasks')
    else:
        form = work_form()
        return render(request, 'addwork.html', {'workform': form})


# # use for getting all files in instruction model relating to job from Activities model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
