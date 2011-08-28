from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from techtips.tips.feeds import TechTipsFeed
from techtips.tips.views import TipListView, TipDetailView, add_tip


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TipListView.as_view(), name='tip_list_view'),
    url(r'^tip/(?P<slug>[\w\-_]+)/$', TipDetailView.as_view(), 
        name='tip_detail_view'),
    url(r'^tip/(?P<slug>[\w\-_]+)/ajax/$', 
        TipDetailView.as_view(template_name='tips/tip_detail_ajax.html'), 
        name='tip_detail_ajax_view'),
    (r'^new/$', add_tip),
    
    (r'^feed/$', TechTipsFeed()),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
