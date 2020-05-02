from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import *


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
        form = job_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('activities')

    else:
        form = job_form(instance=jobid)
        print(form)
        print(job_form)
        print(task)
        # print(form, ' attributes of part object ')
        return render(request, 'detail.html', {'form': form})

# # use for getting all files in instruction model relating to job from jobs model
# some_manual = Manual.objects.get(id=1)
# some_manual_pdfs = some_manual.manualpdf_set.all()
