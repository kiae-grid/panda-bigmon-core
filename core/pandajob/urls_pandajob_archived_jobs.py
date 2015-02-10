from django.conf.urls import patterns, include, url

import views as pandajob_views

urlpatterns_pandajob_archived_jobs = patterns('',
#    url(r'^jobs/$', pandajob_views.jobList, name='jobList'),
#    url(r'^jobs/(.*)/$', pandajob_views.jobList, name='jobList'),
#    url(r'^jobs/(.*)/(.*)/$', pandajob_views.jobList, name='jobList'),
    url(r'^$', pandajob_views.archived_jobList, name='archivedJobList'),
    url(r'^(.*)/$', pandajob_views.archived_jobList, name='archivedJobList'),
    url(r'^(.*)/(.*)/$', pandajob_views.archived_jobList, name='archivedJobList'),
)
urlpatterns = urlpatterns_pandajob_archived_jobs