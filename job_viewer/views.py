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

def db_delete(job_id):
    print('Excluding {}'.format(job_id))
    job = Job.objects.get(pk=job_id)
    job.delete()

def delete(request, job_id):
    db_delete(job_id)
    return redirect('job_viewer:index')

def archive(request, job_id):
    print('Archiving {}'.format(job_id))
    job = Job.objects.get(pk=job_id)
    job.archived = True
    job.save()
    return redirect('job_viewer:index')

def show_archived(request, job_pos):
    template = loader.get_template('archived.html')
    try:
        if not job_pos:
            job_pos = 0
        job = Job.objects.filter(archived = True).order_by('date')[int(job_pos)]
        context = { 'job': job, 'job_pos': job_pos }
    except IndexError:
        context = {}
    return HttpResponse(template.render(context, request))

def delete_archived(request, job_id, job_pos):
    db_delete(job_id)
    print('job_pos=' + str(job_pos))
    return redirect('job_viewer:show_archived', job_pos=job_pos)

