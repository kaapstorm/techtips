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
    