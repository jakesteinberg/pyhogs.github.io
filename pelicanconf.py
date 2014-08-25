#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'JP Rinehimer'
SITENAME = u'PyHOGS'
SITEURL = '' # Set in publishconf.py

# Content licensing: CC-BY
CC_LICENSE = "CC-BY-SA"
CC_ATTR_MARKUP = True

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('Numpy', 'http://www.numpy.org'),
         ('Interesting notebooks', 'https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks'),
         ('Enthought Canopy', 'https://www.enthought.com/products/canopy/'),
         ('python4oceanographers', 'http://ocefpaf.github.io/python4oceanographers/'),
         ("EarthPy", "http://earthpy.org/"),
         ('pyAOS', 'http://pyaos.johnny-lin.com/'),
         ('Ocean Python', 'http://oceanpython.org/'),
         ('SEAPY', 'https://code.google.com/p/sea-py/wiki/SEAPY'),
         ('Astropython', 'http://astropython.blogspot.com/'))

# Social widget
SOCIAL = (('Github', 'https://github.com/UWOcnPyUsers/uwocnpyusers'),)
FEEDS = True
GITHUB_URL = "https://github.com/UWOcnPyUsers"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom theme settings
# Here we use just one set of theme files, and version that.  We copy the theme
# from the pelican-theme repo once. Because the theme will be custom for the
# site, it's not going to change often, and when it does those changes will
# likely be less-than-useful for populating back to the master pelican-themes
# repo.
#
# While the pelican project makes a well-meaning attempt to seperate style and
# content, their themes define  and determine quite a bit of the content of the
# site and how it's laid out.
#
# The only issue will be incorporating upstream changes.  Others methods for
# this include submodules and subtrees, both of which are a pain in the arse.
# Any changes we need could easily come from a patch file, or even done by
# hand if need be, so this should not be a huge problem.
#
# Another issue may be changing themes.  Again, this should be easy to do just
# by using git branches for a different theme.
THEME = 'theme'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', ]

# IPython Notebooks configuration
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

PLUGINS += ['liquid_tags.notebook']
NOTEBOOK_DIR = '../uwocnpyusers/notebooks/'
