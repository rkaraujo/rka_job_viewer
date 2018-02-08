from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^next/(?P<job_id>[0-9]+)/$', views.next, name='next'),
    url(r'^archive/(?P<job_id>[0-9]+)/$', views.archive, name='archive'),
]
