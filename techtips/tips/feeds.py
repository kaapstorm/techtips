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

from django.contrib.syndication.views import Feed
from techtips.tips.models import Tip

class TechTipsFeed(Feed):
    title = "Tech Tips"
    link = "/"
    
    def items(self):
        return Tip.objects.filter(is_published=True)\
                          .order_by('-created_at')[:10]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content
    
    def item_link(self, item):
        return item.get_absolute_url()
    