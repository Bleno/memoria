#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bleno Silva'
SITENAME = u'Jogo da Mem\xf3ria'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

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


THEME = 'theme/pelican-materialize-starter/'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


###############################
### Config materialize theme
NAVBARFIXED = True
NAVCOLLOR = 'purple darken-2'
ABOUTCOMPANY = (('Company Bio', """We are a team of college students 
                                working on this project like it's our
                                 full time job. Any amount would help support
                                 and continue development on this project and
                                 is greatly appreciated."""),)

COPYRIGHT = """<div class="container">
                Made by <a class="orange-text text-lighten-3"
                href="http://materializecss.com">Materialize</a>
                </div>"""
                           
