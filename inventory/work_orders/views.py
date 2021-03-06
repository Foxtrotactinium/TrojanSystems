from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import activity_form, required_part_form, task_form, work_form, required_activity_form
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
    activity = get_object_or_404(Activities, id=id)
    if request.method == "POST":
        form = activity_form(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = activity_form(instance=activity)
        context = {'activityform': form,
                   'activitypartsrequired': ActivityRequiredParts.objects.all().filter(activityid=id),
                   'id': id}
        return render(request, 'activityinformation.html', context)


def add_required_part_to_activity(request, id):
    activity_parts = ActivityRequiredParts.objects.all().filter(activityid=id)
    parts = PartsList.objects.all()
    if request.method == "POST":
        form = required_part_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('activities')

    else:
        form = required_part_form(initial={'activityid': id})
        # form.fields['activityid'].disabled = True
        context = {'requiredpartform': form,
                   'activityrequiredparts': activity_parts,
                   'parts': parts,
                   }
    return render(request, 'addrequired.html', context)


def tasks(request):
    return render(request, 'tasks.html', {'header': 'Tasks',
                                          'tasks': Tasks.objects.distinct()})


def add_task(request):
    if request.method == "POST":
        form = task_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks')
        # if form.is_valid():
        #     task_name = form.cleaned_data['task_name']
        #     activity = form.cleaned_data['activityid']
        #
        #     if Tasks.objects.filter(task_name=task_name).count() > 0:
        #         messages.error(request, "Task name exists")
        #         return redirect('addtask')
        #
        #     required_list = ActivityRequiredParts.objects.filter(activityid=activity)
        #     for required in required_list:
        #         temp = TaskRequiredActivities(task_name=task_name,
        #                                       activityid=activity,
        #                                       )
        #         temp.save()
        #     return redirect('tasks')
    else:
        form = task_form()
        return render(request, 'addtask.html', {'taskform': form})


def task_information(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == "POST":
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    else:
        form = task_form(instance=task)
        context = {'taskform': form,
                   'taskactivities': TaskRequiredActivities.objects.filter(task_name=id),
                   'id': id}
        return render(request, 'taskinformation.html', context)


def add_required_activity_to_task(request, id):
    all_activities = Activities.objects.all()
    task_activities = TaskRequiredActivities.objects.filter(task_name=id)
    if request.method == "POST":
        form = required_activity_form(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form)
            form.save()
        return redirect('tasks')

    else:
        form = required_activity_form(initial={'task_name': id})
        # form.fields['task_name'].readonly = True
        # form.fields['task_name'].value = id
        context = {'requiredactivityform': form,
                   'taskrequiredactivity': task_activities,
                   'allactivities': all_activities,
                   }
    return render(request, 'addrequiredactivity.html', context)


def tasks(request):
    return render(request, 'tasks.html', {'header': 'Tasks',
                                          'tasks': Tasks.objects.all()})


def work_centre_list(request):
    return render(request, 'workcentre.html', {'header': 'Outstanding Jobs',
                                               'workcentre': WorkCentre.objects.values_list('vehicle', flat=True).distinct()})


def add_work(request):
    if request.method == "POST":
        form = work_form(request.POST)
        if form.is_valid():
            vehicle = form.cleaned_data['vehicle']

            if WorkCentre.objects.filter(vehicle=vehicle).count() > 0:
                messages.error(request, "Vehicle already exists")
                return redirect('addwork')

            task_name = form.cleaned_data['task_name']
            notes = form.cleaned_data['notes']

            # activity = get_object_or_404(TaskRequiredActivities, task_name=task_name).activityid

            task_activity_list = TaskRequiredActivities.objects.filter(task_name=task_name)

            for activity in task_activity_list:

                required_list = ActivityRequiredParts.objects.filter(activityid=activity.activityid)
                for required in required_list:
                    temp = WorkCentre(vehicle=vehicle,
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

            return redirect('workcentre')
    else:
        form = work_form()
        return render(request, 'addwork.html', {'workform': form})


def work_information(request, vehicle):
    tasks = WorkCentre.objects.filter(vehicle=vehicle).filter(complete=False).values_list('task_name__task_name', flat=True).distinct()
    return render(request, 'workcentretasks.html', {'header': 'Outstanding Tasks',
                                                    'vehicle': vehicle,
                                                    'workcentretasks': tasks})


def work_task_information(request, vehicle, task):
    activities = WorkCentre.objects.filter(vehicle=vehicle).filter(complete=False).values_list('activityid__activityid', flat=True).distinct()
    return render(request, 'workcentretasksactivities.html', {'header': 'Kits',
                                                              'taskactivities': activities,
                                                              'vehicle':vehicle,
                                                              'task':task})

def work_task_activity_information(request, vehicle, task, activity):
    # needed_activities = Activities.objects.filter(activityid=activity)
    needed_activities = get_object_or_404(Activities,activityid=activity)
    parts = WorkCentre.objects.filter(vehicle=vehicle).filter(complete=False).filter(
        activityid=needed_activities)
    return render(request, 'workcentretaskactivityparts.html', {'header': 'Kits',
                                                                'vehicle':vehicle,
                                                                'task':task,
                                                                'activity':activity,
                                                                'parts': parts})

# # use for getting all files in instruction model relating to job from Activities model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
