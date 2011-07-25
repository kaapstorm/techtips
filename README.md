TechTips
========

This is a small Django project that allows users to submit tips, and content 
managers to edit and publish them.

Feeds
-----

An RSS2 feed is available at the url "feed/".

Requirements
------------

  * Python-markdown
  
To do
-----

  1. All templates (remember to announce the feed in base.html)
  2. Form validation. See comments in tips/forms.py.
  3. tips/admin.py
  4. Markup for tip.content -- remember to sanitise input -- perhaps at first 
     simply by displaying unpublished tips without filtering tip.content. 
     However, this would prevent a "Preview" facility. 
     
     See [Django docs](https://docs.djangoproject.com/en/1.3/ref/contrib/markup/)
     and [Django wiki](https://code.djangoproject.com/wiki/UsingMarkup).
  5. Comments
