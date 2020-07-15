from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import activity_form, required_form, task_form


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
    print(id)
    if request.method == "POST":
        form = activity_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = activity_form(initial={'activityid': task})
        return render(request, 'activityinformation.html',
                      {
                          'activityform': form,
                          'activitypartsrequired': ActivityRequiredParts.objects.all().filter(activityid=id),
                          'id': id
                      })


def add_required_part_to_activity(request, id):
    required_parts_for_activity = ActivityRequiredParts.objects.all().filter(activityid=id)
    parts = PartsList.objects.all()
    if request.method == "POST":
        form = required_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = required_form(initial={'activityid': get_object_or_404(ActivityRequiredParts, activityid=id)})
        form.fields['activityid'].disabled = True
        return render(request, 'addrequired.html', {'requiredpartform': form,
                                                    'activityrequiredparts': required_parts_for_activity,
                                                    'parts': parts,
                                                    })


def tasks(request):
    return render(request, 'tasks.html', {'header': 'Tasks',
                                          'tasks': Tasks.objects.all().filter(complete=False)})


def add_task(request):
    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            activity = form.cleaned_data['activityid']

            if Tasks.objects.all().filter(task_name=task_name).count() > 0:
                ctx = {}
                ctx['form_errors'] = "Activity name exists"
                ctx['taskform'] = task_form()
                return render(request, 'addtask.html', ctx)

            required_list = ActivityRequiredParts.objects.all().filter(activityid=activity)
            for required in required_list:
                temp = Tasks(task_name=task_name,
                             activityid=activity,
                             partsrequired=required.partsrequired,
                             increment=required.increment,
                             quantityrequired=required.quantityrequired,
                             quantitycompleted=0,
                             user=request.user,
                             complete=False,
                             )
                temp.save()
                print(temp)
            return redirect('tasks')
    else:
        form = task_form()
        return render(request, 'addtask.html', {'taskform': form})

# # use for getting all files in instruction model relating to job from Activities model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
