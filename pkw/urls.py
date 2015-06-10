from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'komisje.views.home', name='home'),
    url(r'^w_(?P<woj_id>\d+)/$', 'komisje.views.woj', name='woj'),
    url(r'^p_(?P<pow_id>\d+)/$', 'komisje.views.powiat', name='powiat'),
    url(r'^g_(?P<gm_id>\d+)/$', 'komisje.views.gmina', name='gmina'),
    url(r'^zapisz_(?P<okr_id>\d+)$', 'komisje.views.zapisz', name='zapisz'),
    # ajax
    url(r'^ajax/update$', 'komisje.views.ajax_update', name='ajax_update'),
    url(r'^ajax/save$', 'komisje.views.ajax_save', name='ajax_save'),
    url(r'^admin/', include(admin.site.urls)),
)
