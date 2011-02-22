from django.conf.urls.defaults import patterns

urlpatterns = patterns('packages.views',
    (r'^$',                     'groups', {}, 'groups-list'),
    (r'^(?P<arch>[A-z0-9]+)/$', 'groups'),
    (r'^(?P<arch>[A-z0-9]+)/(?P<name>[A-z0-9\-+.]+)/$', 'group_details'),
)

# vim: set ts=4 sw=4 et: