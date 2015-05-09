from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'komisje.views.home', name='home'),
    url(r'^w_(?P<woj_id>\d+)/$', 'komisje.views.woj', name='woj'),
    url(r'^p_(?P<pow_id>\d+)/$', 'komisje.views.powiat', name='powiat'),
    url(r'^g_(?P<gm_id>\d+)/$', 'komisje.views.gmina', name='gmina'),
    url(r'^o_(?P<okr_id>\d+)/$', 'komisje.views.okreg', name='okreg'),
    url(r'^zapisz_(?P<okr_id>\d+)$', 'komisje.views.zapisz', name='zapisz'),
    url(r'^admin/', include(admin.site.urls)),
)
