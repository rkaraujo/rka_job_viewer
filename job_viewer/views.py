from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Job

def index(request):
    template = loader.get_template('index.html')
    try:
        job = Job.objects.filter(archived = False).order_by('date')[0]
        context = { 'job': job }
    except IndexError:
        context = {}
    return HttpResponse(template.render(context, request))

def next(request, job_id):
    print('Excluding {}'.format(job_id))
    job = Job.objects.get(pk=job_id)
    job.delete()
    return redirect('job_viewer:index')

def archive(request, job_id):
    print('Archiving {}'.format(job_id))
    job = Job.objects.get(pk=job_id)
    job.archived = True
    job.save()
    return redirect('job_viewer:index')

