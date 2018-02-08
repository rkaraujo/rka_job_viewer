from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete/(?P<job_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^archive/(?P<job_id>[0-9]+)/$', views.archive, name='archive'),
    url(r'^show_archived/(?P<job_pos>[0-9]+)/$', views.show_archived, name='show_archived'),
    url(r'^delete_archived/(?P<job_id>[0-9]+)/(?P<job_pos>[0-9]+)/$', views.delete_archived, name='delete_archived'),
]
