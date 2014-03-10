#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Chris Gibson'
SITENAME = u'Mr Voxel'
SITEURL = '/Users/cgibson/Projects/mrvoxel_blog/output'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = "%b %d, %Y"

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

SITE_MAP = "site-map.lua"

SLUG_REDIRECT = True

DEFAULT_PAGINATION = 5

PLUGIN_PATH = 'plugins'

PLUGINS = ["sitemap"]

THEME = 'theme'

#DISQUS_SITENAME = 'mrvoxel.com'
#GITHUB_URL = 'github.com/cgibson'
#TWITTER_USERNAME = 'mrvoxel'
