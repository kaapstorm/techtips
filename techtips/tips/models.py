from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Tip(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tip_detail_view', slug=self.slug)
