from django.conf.urls.defaults import patterns, include, url
from Coordinate.events.models import *
from Coordinate.locations.models import*


from django.contrib import admin
admin.autodiscover()
admin.site.register(Event)
admin.site.register(Association)
admin.site.register(Participant)
admin.site.register(SponsorModel)
admin.site.register(SponsorLevel)
admin.site.register(Location)
admin.site.register(Floorplan)
admin.site.register(Boothspace)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Coordinate.views.home', name='home'),
    # url(r'^Coordinate/', include('Coordinate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
