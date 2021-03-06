from django.conf.urls import patterns, include, url
from reports.views import ReportListAPIView, ReportRetrieveAPIView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamdash.views.home', name='home'),
    # url(r'^teamdash/', include('teamdash.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/report/$', ReportListAPIView.as_view(), name='list'),
    url(r'^api/report/(?P<pk>\d+)/$', ReportRetrieveAPIView.as_view(), name='retrieve')
)
