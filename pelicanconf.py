#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrian Torrie'
SITENAME = 'adriantorrie.github.io'
SITESUBTITLE = 'Python Data Science and Machine Learning portfolio.'
SITEURL = 'https://adriantorrie.github.io'
CATEGORY_URL = 'category/{slug}.html'

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/adriantorrie'),
          ('Stackoverflow', 'http://stackoverflow.com/story/adriantorrie'),
          ('LinkedIn', 'https://au.linkedin.com/in/adriantorrie'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Content admin
# STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
STATIC_PATHS = ['images', 'figures', 'downloads']
IGNORE_FILES = ['*.ipynb_checkpoints']

# Theme and plugins
# For a list and description of plugins visit:
# https://github.com/getpelican/pelican-plugins/blob/master/Readme.rst
# THEME = "themes/elegant"
# THEME = "themes/nice-blog"
THEME = "themes/tuxlite_tbs"
# PYGMENTS_STYLE = 'monokai'

MARKUP = ('md', )
PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = ['ipynb.liquid', 'summary']
# PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.include_code', 'liquid_tags.notebook',
#            'liquid_tags.literal']

# other
TYPOGRIFY = True