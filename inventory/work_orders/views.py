from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import JobForm, RequiredForm


# Create your views here.
def activity_list(request):
    tasks = jobs.objects.all()
    template = loader.get_template('activities.html')
    context = {
        'tasks': tasks,
        'header': 'Activities'
    }
    return HttpResponse(template.render(context, request))


def job_information(request, jobid):
    task = get_object_or_404(jobs, jobid=jobid)

    if request.method == "POST":
        form1 = JobForm(request.POST, instance=task)
        form2 = RequiredForm(request.POST, instance=task)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('activities')

    else:
        form1 = JobForm(instance=task)
        form2 = RequiredForm(instance=task)
        return render(request, 'workinfo.html', {'jobForm': form1, 'requiredForm': form2})

# # use for getting all files in instruction model relating to job from jobs model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
