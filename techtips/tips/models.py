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

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Tip(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content_markdown = models.TextField(help_text='Use Markdown syntax')
    content = models.TextField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tip_detail_view', kwargs={'slug': self.slug})
    
    def save(self):
        """Converts markdown to safe HTML. HTML tags in Markdown are escaped.
        """
        # Useful: https://code.djangoproject.com/wiki/UsingMarkup
        # See also:
        # http://pypi.python.org/pypi/django-markupfield/
        # http://www.martin-geber.com/thought/2007/10/27/markdown-syntax-highlighting-django/
        import markdown
        # Strip tags to ensure it is safe. Then convert markdown to HTML.
        self.content = markdown.markdown(self.content_markdown, 
                                         safe_mode='escape')
        super(Tip, self).save()
    
    class Meta:
        ordering = ['-created_at']
