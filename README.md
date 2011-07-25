TechTips
========

This is a small Django project that allows users to submit tips, and content 
managers to edit and publish them.

Tips are listed on an index page, and details are visible on a details page.

Feeds
-----

A feed is available at the url "feed/".

Requirements
------------

  * Python-markdown
  
To do
-----

  1. All templates (remember to announce the feed in base.html)
  2. Form validation
  3. tips/admin.py
  4. Markup for tip.content -- REMEMBER TO SANITISE INPUT
     cf. https://docs.djangoproject.com/en/1.3/ref/contrib/markup/
     cf. https://code.djangoproject.com/wiki/UsingMarkup
  5. Comments
