#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shannon Moran'
SITENAME = "Shannon Moran"
SITEURL = ''

# Add in themes
THEME = 'themes/moran'
ABOUT_PAGE = '/pages/about.html'
CV_PAGE = '/pages/cv.html'
PUBLICATIONS_PAGE = '/pages/publications.html'
SHOW_ARCHIVES = True

PATH = 'content'
FAVICON = 'images/favicon.ico'
STATIC_PATHS = [
    'images',
    'pdfs',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
TWITTER_USERNAME = 'shannoninshort'
GITHUB_USERNAME = 'shannon-moran'
SOCIAL = (('github', 'http://github.com/shannon-moran'),
          ('google scholar', 'https://scholar.google.com/citations?user=4HxxyckAAAAJ&hl=en&oi=ao'),
          ('twitter', 'http://twitter.com/shannoninshort'),
          ('linkedin', 'https://www.linkedin.com/in/shannonemoran/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# 01/28/2018: Added per tutorial at https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['ipynb.markup','render_math']
