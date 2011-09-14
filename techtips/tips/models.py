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

import markdown

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Tip(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content_markdown = models.TextField(verbose_name='Content (Markdown-formatted)',
                                        help_text='Use <a href="http://daringfireball.net/projects/markdown/">Markdown</a> syntax')
    content = models.TextField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tip_detail_view', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        """Converts markdown to safe HTML, and creates unique slug.
        """
        # Useful: https://code.djangoproject.com/wiki/UsingMarkup
        # See also:
        # http://pypi.python.org/pypi/django-markupfield/
        # http://www.freewisdom.org/projects/python-markdown/CodeHilite
        # Enable extra features. Escape tags.
        self.content = markdown.markdown(self.content_markdown, ['extra'],
                                         safe_mode='escape')
        # Check slug is unique
        if self.slug is None or len(self.slug) == 0:
            self.slug = slugify(self.title)
        initial_slug = self.slug
        serial = 1
        while Tip.objects.filter(slug=self.slug).count() > 0:
            serial += 1
            self.slug = '%s-%s' % (initial_slug, serial)
        super(Tip, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']
