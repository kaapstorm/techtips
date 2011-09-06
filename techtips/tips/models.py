from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags


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
        import markdown
        # Strip tags to ensure it is safe. Then convert markdown to HTML.
        self.content = markdown.markdown(strip_tags(self.content_markdown))
        super(Tip, self).save()
    
    # Useful: https://code.djangoproject.com/wiki/UsingMarkup
    # See also:
    # http://pypi.python.org/pypi/django-markupfield/
    # http://www.martin-geber.com/thought/2007/10/27/markdown-syntax-highlighting-django/
    