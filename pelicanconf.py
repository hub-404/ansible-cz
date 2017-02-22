#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'.'
SITENAME = u'ansible.cz'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'cz'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SHOW_DATE_MODIFIED = False
SHOW_DATE_PUBLISHED = False

# Blogroll
LINKS = (('Ansible.com', 'http://ansible.com/'),
         ('David Karban', 'http://davidkarban.cz/'),
         ('Věroš Kaplan', 'http://veroskaplan.cz/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

THEME = 'themes/bootstrap3'

SUMMARY_MAX_LENGTH = None

GOOGLE_ANALYTICS = 'UA-68681254-1'
