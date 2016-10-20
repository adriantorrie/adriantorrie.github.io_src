#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrian Torrie'
SITENAME = 'adriantorrie.github.io'
SITESUBTITLE = 'Python Data Science and Machine Learning portfolio.'
SITEURL = ''

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Content admin
# STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
STATIC_PATHS = ['images', 'figures', 'downloads']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
# For a list and description of plugins visit:
# https://github.com/getpelican/pelican-plugins/blob/master/Readme.rst
THEME = "themes/Flex"
PYGMENTS_STYLE = 'monokai'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']
