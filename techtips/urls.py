# This file is part of Tech Tip of the Day.
# 
# Tech Tip of the Day is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tech Tip of the Day is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tech Tip of the Day.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from techtips.tips.feeds import TechTipsFeed
from techtips.tips.views import TipListView, TipDetailView, add_tip


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TipListView.as_view(), 
        name='tip_list_view'),
    url(r'^tip/(?P<slug>[\w\-_]+)/$', TipDetailView.as_view(), 
        name='tip_detail_view'),
    url(r'^tip/(?P<slug>[\w\-_]+)/ajax/$', 
        TipDetailView.as_view(template_name='tips/tip_detail_ajax.html'), 
        name='tip_detail_ajax_view'),
    # (r'^new/$', add_tip),
    
    url(r'^feed/$', TechTipsFeed(), 
        name='feed'),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
